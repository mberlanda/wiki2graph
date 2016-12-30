import re
from utilities import flatten_all
import pdb

class Page():
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
    def merge_links_and_title(p):
        l = p.links
        l.append(p.title)
        return l

    @staticmethod
    def unique_from_list(page_list):
        lst = map(lambda p: Page.merge_links_and_title(p), page_list)
        return list(set(flatten_all(lst)))