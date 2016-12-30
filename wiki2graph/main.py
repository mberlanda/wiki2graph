#!/usr/bin/python
# -*- coding: latin-1 -*-

from wiki2graph import *
import pdb

file_path = 'data/chunk-1.xml.bz2'

if __name__ == '__main__':
    pages = Parser().process_file_to_pages(file_path)
    page_list = map(lambda x: Page(x), pages)
    page_unique = Page.unique_from_list(page_list)

    pdb.set_trace()