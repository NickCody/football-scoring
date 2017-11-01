"""
Program that determines individual football scores
based on a target score. So 10 might yield (3, 7)
"""

SCORING = (7, 3, 2)

def combine(total_score):
    """ function that returns a tuple of points that add up to target score"""

    # This small optimization skips a lot of subtrees that don't wind up
    # getting selected anyway since we return only the first solution[0].
    # below... as a result we can easily handle very large scores since
    # Any score above 9 just selects 7 (lame)
    if total_score >= 9:
        optimized_scoring = (7,)
    else:
        optimized_scoring = scoring

    if total_score >= 9:
        optimized_scoring = (7,)
    else:
        optimized_scoring = SCORING

    possibles = map(lambda points: combine(total_score - points) + (points,), optimized_scoring)
    solutions = filter(lambda series: sum(series) == total_score, possibles)

    if solutions:
        return solutions[0]
    else:
        return ()

if __name__ == "__main__":
    while True:
        SCORE = input("Enter an integer greater than 1:")
        print combine(SCORE)
