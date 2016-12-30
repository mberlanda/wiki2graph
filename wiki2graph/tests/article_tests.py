from wiki2graph import Article
import unittest

class ArticleTest(unittest.TestCase):

    def setUp(self):
        text = """
        <title> abc </title>
        123
        456
        [[link1]]
        789
        [[  link2  ]]        
        1515
        [[link2]]
        [[link to: be excluded]]
        """
        self.article = Article(text)

    def test_title(self):
        self.assertEqual(self.article.title, 'abc')

    def test_links(self):
        self.assertEqual(self.article.links, ['link1', 'link2', 'link2'])

    def test_unique_from_list(self):
        lst = [self.article, self.article]
        actual = Article.unique_from_list(lst)
        self.assertEqual(actual, ['abc','link1', 'link2'])

    def test_relations_from_list(self):
        lst = [self.article, self.article]
        actual = Article.relations_from_list(lst)
        self.assertEqual(actual, [('abc', 'link2'), ('abc', 'link1')])


if __name__ == '__main__':
    unittest.main()