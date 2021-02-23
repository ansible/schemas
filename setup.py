#! /usr/bin/env python3
import setuptools

setuptools.setup(
    use_scm_version={"local_scheme": "no-local-version"},
    setup_requires=["setuptools_scm[toml]>=3.5.0"],
)
