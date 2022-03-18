import * as assert from 'assert';
import * as path from 'path';
import Ajv from "ajv"
import fs from 'fs';
import minimatch from 'minimatch';
import yaml from 'js-yaml';

const ajv = new Ajv({
  strictTypes: false,
  strict: false,
  inlineRefs: true,  // https://github.com/ajv-validator/ajv/issues/1581#issuecomment-832211568
  allErrors: true  // https://github.com/ajv-validator/ajv/issues/1581#issuecomment-832211568
});

// load whitelist of all test file subjects schemas can reference
const example_files = getAllFiles('./examples');

// load all schemas
const schema_files = fs.readdirSync("f/").filter(el => path.extname(el) === '.json');
console.log(`Schemas: ${schema_files}`);

describe('schemas under f/', function () {
  schema_files.forEach(schema_file => {
      const schema_json = JSON.parse(fs.readFileSync(`f/${schema_file}`, 'utf8'));
      const validator = ajv.compile(schema_json);
      if (schema_json.examples == undefined) {
        console.error(`Schema file ${schema_file} is missing an examples key that we need for documenting file matching patterns.`);
        return process.exit(1);
      }
      describe(schema_file, function() {
        getTestFiles(schema_json.examples).forEach(({ file: test_file, expect_fail }) => {
          it(`linting ${test_file}`, function () {
            const result = (validator(yaml.load(fs.readFileSync(test_file, 'utf8'))) ? !expect_fail : expect_fail);
            if (!result) console.log(validator.errors)
            assert.strictEqual(result, true);
          });
      });
    });
  });
});

// find all tests for each schema file
function getTestFiles(globs: string[]): { file: string, expect_fail: boolean }[] {
  const files = Array.from(new Set(globs
    .map((glob: any) => minimatch.match(example_files, path.join('**', glob)))
    .flat()));
  return files.map(f => ({ file: f, expect_fail: fs.existsSync(`${f}.fail`) }));
}

function getAllFiles(dir: string): string[] {
  return fs.readdirSync(dir).reduce((files: string[], file: string) => {
    const name = path.join(dir, file);
    const isDirectory = fs.statSync(name).isDirectory();
    return isDirectory ? [...files, ...getAllFiles(name)] : [...files, name];
  }, []);
}
