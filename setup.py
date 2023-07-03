#!/usr/bin/env python3
# straight up stole this file from https://github.com/geohot/tinygrad/blob/master/setup.py

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fastpandas",
    version="0.0.0",
    description="Faster Pandas with DuckDB and Lazy Evaluation",
    author="xnought",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["fastpandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["pandas", "duckdb"],
    python_requires=">=3.8",
    extras_require={
        # 'llvm': ["llvmlite"],
        # 'cuda': ["pycuda"],
        # 'triton': ["triton>=2.0.0.dev20221202"],
        # 'metal': ["pyobjc-framework-Metal", "pyobjc-framework-Cocoa", "pyobjc-framework-libdispatch"],
        # 'linting': [
        #     "flake8",
        #     "pylint",
        #     "mypy",
        #     "pre-commit",
        # ],
        # 'testing': [
        #     "torch",
        #     "pytest",
        #     "pytest-xdist",
        #     "onnx",
        #     "onnx2torch",
        #     "opencv-python",
        #     "tabulate",
        #     "safetensors",
        #     "types-PyYAML",
        # ],
    },
    include_package_data=True,
)
