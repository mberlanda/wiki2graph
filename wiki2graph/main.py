#!/usr/bin/python
# -*- coding: latin-1 -*-

import lib.parser as p
import pdb
import os
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

file_path = 'data/chunk-1.xml.bz2'

if __name__ == '__main__':
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    with open('tmp/decompressed_file.txt', 'w') as f:
        f.write(p.decompress_file(file_path))

    with open('tmp/decompressed_file.txt') as df:
        data = df.read()
        pages = p.find_pages(data)

    result = {}
    for page in pages:
        result[p.page_title(page)] = p.page_links(page) 
    pdb.set_trace()