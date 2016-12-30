from os import path, makedirs

def flatten_all(iterable):
    for elem in iterable:
        if not isinstance(elem, list):
            yield elem
        else:
            for x in flatten_all(elem):
                yield x

def check_dir(dir_name):
    if not path.exists(dir_name):
        makedirs(dir_name)
    return path.dirname(path.abspath(dir_name +'/*'))