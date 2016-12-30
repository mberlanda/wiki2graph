from bz2 import BZ2File
import re

class Parser():

    def __init__(self):
        pass

    def process_file_to_pages(self, fp):
        decompressed = self.decompress_file(fp)
        return self.find_pages(decompressed)

    def decompress_file(self, fp):
        return BZ2File(fp).read()

    def find_pages(self, string):
        return self.page_pattern().findall(string.replace('\n', ''))
    
    def page_pattern(self):
        return re.compile('<page>(.*?)</page>', re.DOTALL)

