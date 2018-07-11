# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="py_ecc",
    ext_modules=cythonize("py_ecc/cython_src/*.pyx")
)
