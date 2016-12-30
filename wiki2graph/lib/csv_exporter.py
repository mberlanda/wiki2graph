import csv
from os import path
from time import time
from utilities import check_dir


class CsvExporter():

    def __init__(self):
        pass

    def unique_articles(self, article_list):
        dir_name = check_dir('tmp')
        file_name = 'unique_articles_{0}.csv'.format(int(time()))
        file_path = path.join(dir_name, file_name)

        with open(file_path, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['article'])
            [ writer.writerow([a]) for a in article_list]

        return file_path

    def article_links(self, article_link_list):
        dir_name = check_dir('tmp')
        file_name = 'article_links_{0}.csv'.format(int(time()))
        file_path = path.join(dir_name, file_name)

