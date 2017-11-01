"""
Program that determines individual football scores
based on a target score. So 10 might yield (3, 7)
"""

# The kinds of scores we support: touchdown, field goal, safety
VALID_POINTS = (7, 3, 2)

def combine(total_score):
    """ function that returns a tuple of points that add up to target score"""

    if total_score <= 0:
        return ()

    possibles = map(lambda points: combine(total_score - points) + (points,), VALID_POINTS)
    solutions = filter(lambda series: sum(series) == total_score, possibles)

    if solutions:
        return solutions[0]
    else:
        return ()

if __name__ == "__main__":
    while True:
        SCORE = input("Enter an integer greater than 1:")
        print combine(SCORE)
