#!/usr/bin/python
# -*- coding: latin-1 -*-

from wiki2graph import *
import pdb

file_path = 'data/chunk-1.xml.bz2'

if __name__ == '__main__':
    pages = Parser().process_file_to_pages(file_path)
    article_list = map(lambda x: Article(x), pages)
    article_unique = Article.unique_from_list(article_list)

    unique_articles_csv = CsvExporter().unique_articles(article_unique)
