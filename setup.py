#!/usr/bin/env python

from setuptools import setup

setup(
    name="tap-sybase",
    version="1.0.12",
    description="Singer.io tap for extracting data from SQL Server - PipelineWise compatible",
    author="Stitch",
    url="https://github.com/s7clarke10/tap-sybase",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    py_modules=["tap_sybase"],
    install_requires=[
        "attrs>=24.2.0",
        "pendulum>=1.2.0",
        "realit-singer-python>=5.0.0",
#        pymssql==2.2.8 broken: https://github.com/pymssql/pymssql/issues/833
        "pymssql>=2.1.4,!=2.2.8",
        "backoff>=1.8.0",
    ],
    entry_points="""
          [console_scripts]
          tap-sybase=tap_sybase:main
      """,
    packages=["tap_sybase", "tap_sybase.sync_strategies"],
)
