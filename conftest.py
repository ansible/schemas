# -*- coding: utf-8 -*-
"""Dynamically creates tests for all schemas and example files."""
# pylint: disable=protected-access
from __future__ import print_function

import logging
import os
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import pytest
from ansiblelint.config import options
from ansiblelint.file_utils import kind_from_path

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.nodes import Node

LOGGER = logging.getLogger(__name__)


def pytest_configure(config: "Config") -> None:  # pylint: disable=unused-argument
    """Configure pytest hook."""


def pytest_collect_file(parent, path) -> Optional["Node"]:
    """Transform each found molecule.yml into a pytest test."""

    # additional mappings not known by ansible-lint (yet)
    options.kinds.insert(  # pylint: disable=no-member
        0, {"zuul": "**/zuul.d/*.{yaml,yml}"}
    )
    options.kinds.insert(0, {"zuul": "**/.zuul.yaml"})  # pylint: disable=no-member

    if path.ext in (".yaml", ".yml") and path.fnmatch("*/examples/*"):
        return YamlFile.from_parent(parent, fspath=path)  # type: ignore
    if path.ext == ".json" and path.fnmatch("f/*.json"):
        return SchemaFile.from_parent(parent, fspath=path)  # type: ignore

    return None


class YamlFile(pytest.File):
    """Wrapper class for YAML examples."""

    def collect(self):
        """Test generator."""
        yield YamlItem.from_parent(self, name="validate", spec="x")

    def __str__(self):
        """Return test name string representation."""
        return str(self.fspath.relto(os.getcwd()))


class SchemaFile(pytest.File):
    """Wrapper class for JSON schema files."""

    def collect(self):
        """Test generator."""
        yield JSONSchemaItem.from_parent(self, name="validate", spec="x")

    def __str__(self):
        """Return test name string representation."""
        return str(self.fspath.relto(os.getcwd()))


class JSONSchemaItem(pytest.Item):
    """A JSON Schema file to be tested."""

    def __init__(self, name, parent, spec):
        """Constructor."""
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self):
        file = Path(self.fspath)
        cmd = [
            "npm",
            "run",
            "--silent",
            "ajv",
            "--",
            "compile",
            "-s",
            str(file),
        ]
        result = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        if result.returncode != 0:
            raise ValidationException(self, result)

    def repr_failure(self, excinfo) -> str:  # type: ignore
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, ValidationException):
            result = excinfo.value.result
            if result:
                cmd = " ".join(result.args)
                return "\n".join(
                    [
                        f"validation command failed with code {result.returncode}",
                        f"   cmd: {cmd}",
                        result.stderr,
                        result.stdout,
                    ]
                )
        return str(excinfo)

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"


class YamlItem(JSONSchemaItem):
    """A YAML file to be tested."""

    def runtest(self):
        file = Path(self.fspath)
        schema = kind_from_path(file)
        if schema not in ["tasks", "vars", "playbook", "meta", "requirements", "zuul"]:
            raise ValidationException(
                self, f"{file} ({schema}) as it did not match any known schemas."
            )
        # https://github.com/ajv-validator/ajv-cli
        cmd = [
            "npm",
            "run",
            "--silent",
            "ajv",
            "--",
            "validate",
            "--strict=false",
            "--errors=json",  # JSON
            "-s",
            f"f/ansible-{schema}.json",
            "-d",
            str(file),
        ]
        result = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        if result.returncode != 0:
            result_file = file.parent / (file.name + ".json")
            if not result_file.is_file():
                raise ValidationException(result=result)
            expected_result = open(result_file).read()
            # We remove first line due to known bug
            # https://github.com/ajv-validator/ajv-cli/issues/16
            output = result.stderr.split("\n", 1)[-1]
            if output != expected_result:
                raise ValidationException(
                    result=result, expected_result=expected_result
                )


class ValidationException(Exception):
    """Validation error."""

    def __init__(
        self,
        result: Optional[subprocess.CompletedProcess] = None,
        expected_result: Optional[str] = None,
        msg: Optional[str] = None,
    ):
        self.result = result
        self.expected_result = expected_result
        self.msg = msg
        super().__init__()
