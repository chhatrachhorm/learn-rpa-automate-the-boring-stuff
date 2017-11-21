#! python3
# ways to represent different people
# and their preferences
from math import sqrt

# a set of movies rate by different people
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
        'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5
    },
    'Toby': {
        'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    },
    'Chhatra': {
        'Harry Potter': 5, 'The Emoji': 5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0
    },
    'Chhorm': {
        'Harry Potter': 5, 'The Emoji': 5, 'Hotel Trans.': 2.5, 'Lion king': 5
    }
}


# ecludean's distance score
# return a distance-based similarity score for 2 people
# movies will be the axes
# people will be the points
def sim_distance(prefs, person1, person2):
    # shared item
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    # add the square of all differences
    sum_of_squares = sum([
        pow(prefs[person1][item] - prefs[person2][item], 2)
        for item in prefs[person1] if item in prefs[person2]
    ])
    # to make result is between 0 and 1
    # compare result with 1 (divide by 1)
    # to avoid divide by 0, add 1 to the sqrt(result) above
    return 1 / (1 + sqrt(sum_of_squares))


# Pearson Correlation Score
# Correlation Coefficient is a measure of how well
# two sets of data fit on a straight line
# people will be the axes
# movies will be the points
# more: https://youtu.be/ugd4k3dC_8Y
# score varies based on x-scatter/y-scatter
# Pearson Correlation Coefficient r
# r = (nSum(xy) - Sum(x)Sum(y))/(sqrt(nSum(x**2)-Sum(x)**2).sqrt(nSum(y**2)-Sum(y)**2))
# where n is the number of sample
# x = xi (i = 0, 1 ..)
# y = yi (i = 0, 1 ..)
def sim_pearson(prefs, p1, p2):
    # get the list of mutually rated item
    similar = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            similar[item] = 1

    n = len(similar)
    if n == 0:
        return 0

    # add all preference, Sum(x) Sum(y)
    sumx = sum([prefs[p1][it] for it in similar])
    sumy = sum([prefs[p2][it] for it in similar])

    # Sum(x**2) Sum(y**2)
    sumx_sqr = sum([pow(prefs[p1][it], 2) for it in similar])
    sumy_sqr = sum([pow(prefs[p2][it], 2) for it in similar])

    # Sum(xy)
    sumxy = sum([prefs[p1][it] * prefs[p2][it] for it in similar])

    # score
    num = n * sumxy - sumx * sumy
    den = (sqrt(n * sumx_sqr - sumx ** 2)) * (sqrt(n * sumy_sqr - sumy ** 2))
    if den == 0:
        return 0
    return num / den


# Ranking
# returns the best match for a person
# number of results and similarity fun() are optional params
def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    # sort and reverse - top first
    scores.sort()
    scores.reverse()
    return scores[:n]


# Recommendations
# Decision Making Type: Weighted Score
# https://www.youtube.com/watch?v=FefJ1paq750 && https://www.youtube.com/watch?v=WpLXbV0jm9c
# In this scenario, to recommend (and rank) a set of movie to a particular users
# we focus of Weighted Score, in which
# the similarity scores of the user and the others are the decision making factors (the value is weighting)
# the movies and the rating scores are the options (value is the score for each)
# to find out the set of recommendations is to find out the weighted decision
# however, to improve the accuracy and tendency in which a movie is overrated or underrated
# we have to compare the real weighted decision score to the overall weighting score
# set of recommendations = weighted decision score / overall weighting score
# e.g.
#
# (Factors)   (WeightingScore)  -------------------Option Score-----------------------
# Critic        Similarity      Night   Sim*Night   Lady     Sim*Lady  Luck    Sim*Luck
# Rose          0.99            3.0     2.97        2.5      2.48      3.0     2.97
# Seymour       0.38            3.0     1.14        3.0      1.14      1.5     0.57
# Puig          0.89            4.5     4.02                           3.0     2.68
# LaSalle       0.92            3.0     2.77        3.0      2.77      2.0     1.85
# Matthews      0.66            3.0     1.99        3.0      1.99
# -------------------------------------------------------------------------------------
# Total                                 12.89                8.38              8.07  <= weighted decision score
# SSum                                  3.84                 2.95              3.18  <= overall weighting score
# Total/SSum                            3.35                 2.83              2.53  <= Final Decision
#
# KeyTerm:
# S = Similarity = Sim
# SSum = Sum of the similarity score of the people who rates the movie
# program
def get_recommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    ssum = {}
    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue
        for item in prefs[other]:
            # only movie the person hasn't seen like other
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # sum of similarity or overall weighting score
                ssum.setdefault(item, 0)
                ssum[item] += sim
    # normalized list
    rankings = [
        (total / ssum[item], item) for item, total in totals.items()
    ]
    # return the sorted list only
    rankings.sort()
    rankings.reverse()
    return rankings
