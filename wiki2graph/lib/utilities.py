from itertools import chain
from collections import Iterable

def flatten(l):
    return list(chain.from_iterable(flatten_helper(x) for x in l))

def flatten_helper(l):
    if isinstance(l, Iterable) and not isinstance(l, basestring):
        return l
    else:
        return [l]

def flatten_all(iterable):
    for elem in iterable:
        if not isinstance(elem, list):
            yield elem
        else:
            for x in flatten_all(elem):
                yield x

def flatten_r(l):
    if not l:
        print 'empty'
        return []
    else:
        try:
            tail = l.pop()
        except IndexError:
            tail = []
        print tail
        if isinstance(tail, Iterable):
            return flatten_r(l) + flatten_r(tail)
        else:
            print len(l)
            return flatten_r(l).append(tail)
