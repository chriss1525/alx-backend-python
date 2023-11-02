#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from utils import *

""" test the test_access_nested_map function """


class TestAccessNestedMap(unittest.TestCase):
    """classs that tests if the test_access_nested_map function works"""
    @parameterized.expand
    def TestAccessNestedMap.test_access_nested_map(self):
        """tests if the function returns the correct value"""
        self.assertEqual(access_nested_map(test, path), 4)
        self.assertEqual(access_nested_map(test, path2), None)
        self.assertEqual(access_nested_map(test, path3), None)
