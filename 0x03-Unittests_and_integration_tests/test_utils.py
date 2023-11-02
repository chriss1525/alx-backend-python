#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from utils import *

""" Test the utils.access_nested_map function """


class TestAccessNestedMap(unittest.TestCase):
    """ Test the utils.access_nested_map function """

    def test_access_nested_map(self):
        """ Test the utils.access_nested_map function """
        nested_map = {'a': 1, 'b': {'c': 2}, 'c': {'d': {'e': 3}}}
        self.assertEqual(access_nested_map(nested_map, ['a']), 1)
        self.assertEqual(access_nested_map(nested_map, ['b']), {'c': 2})
        self.assertEqual(access_nested_map(nested_map, ['c', 'd', 'e']), 3)

    def test_access_nested_map_exception(self):
        """ Test the utils.access_nested_map function """
        nested_map = {'a': 1, 'b': {'c': 2}, 'c': {'d': {'e': 3}}}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ['a', 'b'])
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ['c', 'd', 'f'])


""" Test the utils.get_json function """


class TestGetJson(unittest.TestCase):
    """ Test the utils.get_json function """

    def test_get_json(self):
        """ Test the utils.get_json function """
        self.assertEqual(get_json("http://example.com"), {"test": "test"})
        self.assertRaises(Exception, get_json, "http://holberton.io")


""" Test the utils.memoize function """


class TestMemoize(unittest.TestCase):
    """ Test the utils.memoize function """

    def test_memoize(self):
        """ Test the utils.memoize function """
        class TestClass:
            """ Test the utils.memoize function """

            def a_method(self):
                """ Test the utils.memoize function """
                return 42

            @memoize
            def a_property(self):
                """ Test the utils.memoize function """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, mock.return_value)
            self.assertEqual(test.a_property, mock.return_value)
            mock.assert_called_once()


""" Test the utils.retry function """


class TestRetry(unittest.TestCase):
    """ Test the utils.retry function """

    def test_retry(self):
        """ Test the utils.retry function """
        class TestClass:
            """ Test the utils.retry function """

            def a_method(self):
                """ Test the utils.retry function """
                return True

            @retry
            def a_property(self):
                """ Test the utils.retry function """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=True) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, mock.return_value)
            mock.assert_called_once()


""" Test the utils.call_history function """


class TestCallHistory(unittest.TestCase):
    """ Test the utils.call_history function """

    def test_call_history(self):
        """ Test the utils.call_history function """
        class TestClass:
            """ Test the utils.call_history function """

            def a_method(self):
                """ Test the utils.call_history function """
                return True

            @call_history
            def a_property(self):
                """ Test the utils.call_history function """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=True) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, mock.return_value)
            mock.assert_called_once()
            self.assertEqual(test.a_property.call_history, [True])
