#!/usr/bin/python
# -*- coding: latin-1 -*-

from wiki2graph import *
import pdb

file_path = 'data/chunk-1.xml.bz2'

if __name__ == '__main__':
    pages = Parser().process_file_to_pages(file_path)
    result = map(lambda x: Page(x), pages)
    pdb.set_trace()