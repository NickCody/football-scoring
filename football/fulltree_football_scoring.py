"""
Determines all possible point combinations for a given score in football
"""

import itertools
flatten = itertools.chain.from_iterable

SCORING = (7, 3, 2)

def dist(tupes, i):
    """ Appends i to each tuple in tupes"""
    return tuple(map(lambda one_tup: one_tup + (i,), tupes))

def t2a(tup):
    """ tuple to array """
    return map(lambda v: v, tup)

def combine(total_score):
    """ function that returns a tuple of points that add up to target score"""

    if total_score <= 1:
        return ((),)

    possibles = flatten(map(lambda p: dist(combine(total_score - p), p), SCORING))
    solutions = filter(lambda scores: sum(t2a(scores)) == total_score, possibles)

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
