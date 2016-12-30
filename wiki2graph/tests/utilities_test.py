import wiki2graph.lib.utilities as utl
import unittest

class UtilitiesTest(unittest.TestCase):

    def test_flattenr(self):
        ary = [1, [2, 3], [4, [5, 6]]]
        expected = [1, 2, 3, 4, 5, 6]

        self.assertEqual(utl.flatten_r(ary), expected)