from wiki2graph import Page
import unittest

class PageTest(unittest.TestCase):

    def setUp(self):
        text = """
        <title> abc </title>
        123
        456
        [[link1]]
        789
        [[  link2  ]]        
        1515
        [[link to: be excluded]]
        """
        self.page = Page(text)

    def test_title(self):
        self.assertEqual(self.page.title, 'abc')

    def test_links(self):
        self.assertEqual(self.page.links, ['link1', 'link2'])

if __name__ == '__main__':
    unittest.main()