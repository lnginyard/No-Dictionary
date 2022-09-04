#!/usr/bin/env python3
"""
Unit test cases for nodict.py
Students should not modify this file.
"""

__author__ = "madarp"

import sys
import unittest
import importlib
import inspect

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Ensure python 3+
assert sys.version_info[0] >= 3

# curriculum devs: change this to 'soln.nodict' to test solution
PKG_NAME = 'nodict'


class TestNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.module = importlib.import_module(PKG_NAME)

    def test_node_instance(self):
        """Check if we can create an instance"""
        nd = self.module.Node("Kevin")
        self.assertIsNotNone(nd, "Unable to create a Node instance")

    def test_comparison_eq(self):
        """Check if comparisons work"""
        wallace = self.module.Node("Wallace")
        grommit = self.module.Node("Grommit")
        other_wallace = self.module.Node("Wallace")
        self.assertNotEqual(wallace, grommit)
        self.assertEqual(wallace, other_wallace)

    def test_repr(self):
        """Check if the __repr__ method is correct"""
        melvin = self.module.Node("Melvin")
        self.assertEqual(
            repr(melvin), "Node(Melvin, None)"
        )


class TestNoDict(unittest.TestCase):
    """Main test fixture for nodict module"""
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.module = importlib.import_module(PKG_NAME)

    def test_instance(self):
        """Check if we can create an instance"""
        nd = self.module.NoDict()
        self.assertIsNotNone(nd, "Unable to create a NoDict instance")

    def test_default_buckets(self):
        """Check if NoDict creates 10 buckets by default"""
        d = self.module.NoDict()
        self.assertIsInstance(
            d.buckets, list,
            "The buckets should be a list of lists"
            )
        self.assertEqual(
            len(d.buckets), 10,
            "There should be 10 buckets created by default"
            )

    def test_more_buckets(self):
        """Check if NoDict creates other bucket sizes"""
        d = self.module.NoDict(512)
        self.assertEqual(
            len(d.buckets), 512,
            "There should be 512 buckets created."
            )

    def test_repr(self):
        """Check if the __repr__ method is correct"""
        d = self.module.NoDict(1)  # create a NoDict with just 1 bucket
        self.assertEqual(repr(d), "NoDict.0:[]")

    def test_add(self):
        """Checks the NoDict.add() method"""
        d = self.module.NoDict(1)
        d.add("Ralphie", "BB gun")
        expected_node = self.module.Node("Ralphie", "BB gun")
        actual_node = d.buckets[0][0]
        self.assertEqual(actual_node, expected_node)

    def test_get(self):
        d = self.module.NoDict()
        d.add("Groucho", 50)
        self.assertEqual(d.get("Groucho"), 50)

    def test_key_error(self):
        """Checks if KeyError is raised"""
        d = self.module.NoDict()
        with self.assertRaises(KeyError):
            d.get("Kevin")

    def test_getitem(self):
        """Checks if __getitem__ is implemented"""
        d = self.module.NoDict()
        d.add("Harpo", 52)
        self.assertEqual(d["Harpo"], 52)

    def test_setitem(self):
        """Checks if __setitem__ is implemented"""
        d = self.module.NoDict()
        d["Harpo"] = 52
        self.assertEqual(d.get("Harpo"), 52)

    def check_no_duplicates(self, method='add'):
        """Check that duplicates are not allowed"""
        # New Node of same name: new value should overwrite previous value
        d = self.module.NoDict()
        setitem = d.add
        getitem = d.get

        if method != 'add':
            setitem = d.__setitem__
            getitem = d.__getitem__

        # Need to access the internal buckets for this test
        self.assertIsInstance(
            d.buckets, list,
            "Need to implement a list of buckets named 'buckets'"
            )

        setitem("Zeppo", 54)
        setitem("Zeppo", 56)
        # All buckets should be empty, except one
        expected_empty = len(d.buckets) - 1
        empty_count = 0
        found_bucket = None
        for b in d.buckets:
            if len(b) == 0:
                empty_count += 1
            else:
                found_bucket = b
        self.assertEqual(
            empty_count, expected_empty,
            "All buckets should be empty except for one"
            )

        self.assertIsNotNone(
            found_bucket,
            "There should be only one bucket containing a Node"
            )

        self.assertEqual(
            len(found_bucket), 1,
            "There should only be one Node in one bucket"
            )

        self.assertEqual(
            getitem('Zeppo'), 56,
            "New value of same key should overwrite previous value"
            )

    def test_no_duplicates_add(self):
        return self.check_no_duplicates(method='add')

    def test_no_duplicates_setitem(self):
        return self.check_no_duplicates(method='setitem')

    def test_doc_strings(self):
        """Checking for docstrings on all methods"""
        d = self.module.NoDict()
        for name, func in inspect.getmembers(d, inspect.ismethod):
            self.assertIsNotNone(
                func.__doc__,
                f"Please add a docstring in the {name} method"
            )


if __name__ == '__main__':
    unittest.main()
