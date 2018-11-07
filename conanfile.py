#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostFunctionConan(base.BoostBaseConan):
    name = "boost_function"
    url = "https://github.com/bincrafters/conan-boost_function"
    lib_short_names = ["function"]
    header_only_libs = ["function"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_move",
        "boost_mpl",
        "boost_preprocessor",
        "boost_throw_exception",
        "boost_type_index",
        "boost_type_traits",
        "boost_typeof"
    ]


