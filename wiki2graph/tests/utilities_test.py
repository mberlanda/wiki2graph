import wiki2graph.lib.utilities as utl
import unittest

class UtilitiesTest(unittest.TestCase):

    def test_flatten(self):
        ary = [1, [2, 3], [4, [5, 6]]]
        expected = [1, 2, 3, 4, 5, 6]

        self.assertEqual(list(utl.flatten_all(ary)), expected)