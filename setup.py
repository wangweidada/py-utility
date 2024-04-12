#!/usr/bin/python
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name="ww-py-utility-pkg",
    version="2.3.16",
    url="https://github.com/wangweidada/py-utility.git",
    author="wangwei",
    author_email="378115003@qq.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    platforms="any",
    install_requires=["requests>=2.20.0","matplotlib","opencv-python","numpy","pandas","redis"],
    python_requires=">=3.6",
)