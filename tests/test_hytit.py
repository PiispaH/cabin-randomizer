#!/usr/bin/env python3

import unittest
from cabin_randomizer.cabins import cabins

class TestHytit(unittest.TestCase):
    def test_names_are_unique(self):
        """Tests that the resulting lists still contain unuique names and that the number of names is correct."""
        group1, group2 = cabins(2, ["a", "b", "c", "d", "e", "f", "g", "h"])
        group1 = set(group1)
        group2 = set(group2)

        # Correct amount of names in each result
        self.assertEqual(len(group1), 4)
        self.assertEqual(len(group2), 4)

        # All names are still unique
        self.assertEqual(set(), group1.intersection(group2))

        group1, group2, group3 = cabins(3, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])
        group1 = set(group1)
        group2 = set(group2)
        group3 = set(group3)
        self.assertEqual(len(group1), 4)
        self.assertEqual(len(group2), 4)
        self.assertEqual(len(group3), 4)

        self.assertEqual(set(), group1.intersection(group2, group3))

    def test_invalid_values_handled_correctly(self):
        """Tests that incorrect input values are handled correctly."""
        with self.assertRaises(ValueError):
            cabins(-4, ["a", "b", "c", "d", "e", "f", "g"])
        with self.assertRaises(ValueError):
            cabins(2.0, ["a", "b", "c", "d", "e", "f", "g"])
        with self.assertRaises(ValueError):
            cabins(0, ["a", "b", "c", "d", "e", "f", "g"])
        with self.assertRaises(ValueError):
            cabins(1, ["a", "b", "c", "d", "e", "f", "g"])
        with self.assertRaises(ValueError):
            cabins(2, ["a", "b", "c", "d", "e", "f", "g"])
        with self.assertRaises(ValueError):
            cabins(0, ["a", "b", "c", "d", "e", "f", "g", "h"])
        with self.assertRaises(ValueError):
            cabins(1, ["a", "b", "c", "d", "e", "f", "g", "h"])
        with self.assertRaises(ValueError):
            cabins(2, ["a", "a", "c", "d", "e", "f", "g", "h"])
        with self.assertRaises(ValueError):
            cabins(1, ["a", "b", "c", "d", "e", "f", "g", "h", "i"])
        with self.assertRaises(ValueError):
            cabins(2, ["a", "b", "c", "d", "e", "f", "g", "h", "i"])
