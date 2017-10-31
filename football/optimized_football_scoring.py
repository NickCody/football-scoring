scoring = (7, 3, 2)

def combine(total_score):
  if total_score <= 0:
    return ()

  if total_score >= 9:
    optimized_scoring = (7,)
  else:
    optimized_scoring = scoring

  possibles = map(lambda p: combine(total_score - p) + (p,), optimized_scoring)
  solutions = filter(lambda series: sum(series) == total_score, possibles)

  if len(solutions) > 0:
    return solutions[0]
  else:
    return ()


while True:
  score = input ("Enter an integer greater than 1:")
  print combine(score)