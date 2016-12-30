import re
from utilities import flatten_all

class Article():
    def __init__(self, text):
        self.text = text
        self.title = self.find_title()
        self.links = self.lint_links(self.find_links())

    def find_title(self):
        return self.title_pattern().search(self.text).groups()[0].strip()

    def find_links(self):
        return self.links_pattern().findall(self.text)

    def title_pattern(self):
        return re.compile('<title>(.*?)</title>', re.DOTALL)

    def links_pattern(self):
        return re.compile('\[\[(.*?)\]\]', re.DOTALL)

    def lint_links(self, links):
        filtered = filter(lambda link: ':' not in link, links)
        return map(lambda l: self.lint_link(l), filtered)

    def lint_link(self, link):
        return link.split('|')[0].strip()

    @staticmethod
    def relations_from_list(article_list):
        lst = map(lambda p: Article.tuple_links_and_title(p), article_list)
        return Article.flatten_unique(lst)

    @staticmethod
    def unique_from_list(article_list):
        lst = map(lambda p: Article.merge_links_and_title(p), article_list)
        return Article.flatten_unique(lst)

    @staticmethod
    def flatten_unique(lst):
        return list(set(list(flatten_all(lst))))

    @staticmethod
    def merge_links_and_title(p):
        l = p.links
        l.append(p.title)
        return l

    @staticmethod
    def tuple_links_and_title(p):
        r = []
        t = p.title
        for l in p.links:
            if l > t:
                r.append((t, l))
            else:
                r.append((l, t))
        return r
