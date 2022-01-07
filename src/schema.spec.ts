import * as assert from 'assert';
import * as path from 'path';
import Ajv from "ajv"
import { ValidateFunction } from "ajv";
import fs from 'fs';
import minimatch from 'minimatch';
import yaml from 'js-yaml';

// https://github.com/ajv-validator/ajv/issues/1373
// https://ajv.js.org/strict-mode.html#prevent-unexpected-validation
const ajv = new Ajv({
  strictTypes: false,
  strict: false,
  inlineRefs: true,  // https://github.com/ajv-validator/ajv/issues/1581#issuecomment-832211568
  allErrors: true  // https://github.com/ajv-validator/ajv/issues/1581#issuecomment-832211568
});

let globToValidatorMap: Map<string, ValidateFunction> = new Map();


// load all schemas
fs.readdir("f/", function(err, files) {
  const schemaFiles = files.filter(el => path.extname(el) === '.json')
  schemaFiles.forEach(function (file) {
    let schema_json = JSON.parse(fs.readFileSync(`f/${file}`, 'utf8'));
    const validator = ajv.compile(schema_json);
    if (schema_json.examples == undefined) {
      console.error(`Schema file ${file} is missing an examples key that we need for documenting file matching patterns.`);
      return process.exit(1);
    }
    schema_json['examples'].forEach(function(glob: string) {
      globToValidatorMap.set(glob, validator);
    });
  });
  console.log(`Schemas: ${schemaFiles}`)
})

function lint(file: string): boolean {
  let result = false;
  let found = false;
  let expect_fail = fs.existsSync(`${file}.fail`)
  // determine which validator to use
  for (let key of Array.from(globToValidatorMap.keys())) {
    let pattern = `**/${key}`;
    let match_result = minimatch.match([file], pattern);
    if (match_result.length) {
      let validator = globToValidatorMap.get(key);
      if (validator) {
        let target = yaml.load(fs.readFileSync(file, 'utf8'));
        result = (validator(target) ? !expect_fail : expect_fail);
        if (!result) console.log(validator.errors)
      }
      found = true;
      break;
    }
  }
  if (!found) {
    console.error(`Failed to match file ${file} to a schema pattern.`)
    result = false;
  }

  return result;
}

function getAllFiles(dir: string): string[] {
  return fs.readdirSync(dir).reduce((files: string[], file: string) => {
    const name = path.join(dir, file);
    const isDirectory = fs.statSync(name).isDirectory();
    return isDirectory ? [...files, ...getAllFiles(name)] : [...files, name];
  }, []);
}

describe('add()', function () {
  getAllFiles("examples").forEach(file => {
    if (path.extname(file) === '.yml') {
      it(`linting ${file}`, function () {
        let res = lint(file);
        assert.strictEqual(res, true);
      });
    };
  });
});
