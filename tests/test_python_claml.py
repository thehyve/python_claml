#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `python_claml` module.
"""
import os
import time

import pytest

from python_claml import claml
from python_claml.claml_types import ClaML


class TestPythonClaml(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_small_file(self):
        start = time.perf_counter()
        contents = open('resources/test.xml', 'r').read()
        mid = time.perf_counter()
        classification: ClaML = claml.CreateFromDocument(contents)
        end = time.perf_counter()
        with open('test.log', 'a') as log_file:
            log_file.write('Test 1 took {} s, reading: {}, parsing: {}\n'.format(
                end - start,
                mid - start,
                end - mid
            ))
        assert classification is not None

    large_test_file = 'resources/icd10gm2019syst_claml_20180921.xml'

    @pytest.mark.skipif(not os.path.isfile(large_test_file), reason="large test file not available")
    def test_large_file(self):
        start = time.perf_counter()
        contents = open(TestPythonClaml.large_test_file, 'r').read()
        mid = time.perf_counter()
        classification = claml.CreateFromDocument(contents)
        end = time.perf_counter()
        with open('test.log', 'a') as log_file:
            log_file.write('Test 2 took {} s, reading: {}, parsing: {}\n'.format(
                end - start,
                mid - start,
                end - mid
            ))
        assert classification is not None

    @classmethod
    def teardown_class(cls):
        pass
