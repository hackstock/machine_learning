import math
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
      'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
      'The Night Listener': 3.0},
     'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
      'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 3.5},
     'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
      'Superman Returns': 3.5, 'The Night Listener': 4.0},
     'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
      'The Night Listener': 4.5, 'Superman Returns': 4.0,
      'You, Me and Dupree': 2.5},
     'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 2.0},
     'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
     'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


def sim_distance(prefs,person1,person2):
  similar_items = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      similar_items[item] = 1

  if len(similar_items) == 0 :return 0

  sum_of_squares = sum([math.pow(prefs[person1][item] - prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])

  return 1/(1 + sum_of_squares)


def sim_pearson(prefs,p1,p2):
  similar_items = {}
  for item in prefs[p1]:
    if item in prefs[p2]:
      similar_items[item] = 1

  n = len(similar_items)

  if n == 0: return 0

  sum1 = sum([prefs[p1][item] for item in similar_items])
  sum2 = sum([prefs[p2][item] for item in similar_items])

  sum1Sq = sum([math.pow(prefs[p1][item],2) for item in similar_items])
  sum2Sq = sum([math.pow(prefs[p2][item],2) for item in similar_items])

  pSum = sum([prefs[p1][item] * prefs[p2][item] for item in similar_items])

  num = pSum - (sum1 * sum2 / n)
  den = math.sqrt((sum1Sq - math.pow(sum1,2)/n) * (sum2Sq - math.pow(sum2,2)/n))

  if den == 0: return 0

  r = num/den

  return r

