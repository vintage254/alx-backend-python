#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map 

class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


    """class for testing keyError"""
    @parameterized.expand([
        ({}, ("a",),"a" ),
        ({"a" : 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
        self.assertEqual(str(e.exception), f"'{expected}'")

if __name__ == '__main__':
    unittest.main()
