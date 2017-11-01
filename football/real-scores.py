"""
Program that determines individual football scores
based on a target score. So 10 might yield (3, 7)

Uses more realistic scoring, touchdown is 6, and you can get an extra
point or 2-point conversti on
"""

import itertools
flatten = itertools.chain.from_iterable

SCORING = (7, 3, 2, 6, 1)

def dist(list_of_tup, i):
    """ Appends i to each tuple in tupes"""

    return tuple(map(lambda one_tup: one_tup + (i,), list_of_tup))

def t2a(tup):
    """ tuple to array """
    return map(lambda v: v, tup)

def valid(tup):
    """ Determines if scores are valid, mostly validating a 1 can only be preceded by a 6 """
    if not tup:
        return True
    elif tup[0] == 1:
        return False
    elif tup[0:3] == (6, 1):
        return valid(tup[2:])
    else:
        return valid(tup[1:])

def combine(total_score):
    """ function that returns a tuple of points that add up to target score"""

    if total_score <= 1:
        return ((),)

    possibles = flatten([dist(combine(total_score - p), p) for p in SCORING])
    solutions = [s for s in possibles if sum(t2a(s)) == total_score and valid(s)]

    return solutions

def unique(solutions):
    """Returns only unique combinations by sorting tuple and using set()"""
    sorted_solutions = map(lambda series: tuple(sorted(series)), solutions)
    unique_solutions = set(sorted_solutions)
    return unique_solutions

if __name__ == "__main__":

    SCORE = input("Enter an integer greater than 1 : ")

    print "All Solutions:"
    for series in combine(SCORE):
        print series

    print "Unique Solutions:"
    for series in unique(combine(SCORE)):
        print series
