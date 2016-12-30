from wiki2graph.lib.page import Page
import unittest

class PageTest(unittest.TestCase):

    def setUp(self):
        self.text = """
        <title> abc </title>
        123
        456
        [[link1]]
        789
        """

    def test_initialize(self):
        page = Page(self.text)
        self.assertEqual(page.title, 'abc')

if __name__ == '__main__':
    unittest.main()