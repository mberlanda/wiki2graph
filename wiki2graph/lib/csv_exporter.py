import csv
from os import path
from time import time
from utilities import check_dir


class CsvExporter():

    def __init__(self):
        pass

    def unique_articles(self, article_list):
        file_path = self.generate_filepath('unique_articles')

        with open(file_path, 'wb') as f:
            w = CsvExporter.default_writer(f)
            w.writerow(['article'])
            [ w.writerow([a]) for a in article_list]

        return file_path

    def article_relations(self, article_relations_dict):
        file_path = self.generate_filepath('article_relations')
        
        with open(file_path, 'wb') as f:
            keys = ['source', 'target']
            w = CsvExporter.default_writer(f)
            w.writerow(keys)
            [ w.writerow([d[k] for k in keys]) for d in article_relations_dict]

        return file_path

    def generate_filepath(self, type, folder='tmp'):
        dir_name = check_dir(folder)
        file_name = '{0}_{1}.csv'.format(type, int(time()))
        return path.join(dir_name, file_name)

    @staticmethod
    def default_writer(file):
        return csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
