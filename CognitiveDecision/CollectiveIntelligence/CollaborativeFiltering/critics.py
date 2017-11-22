#! python3

# a set of movies rate by different people
from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.ranking import *
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


# Matching Products
# convert from user => movie to movie => users
# 'Chhatra' : {'The Lion': 3.5 ..} => 'The Lion' : {'Chhatra':3.5..}
def transform_prefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]
    return result
# matching movie
# to match this use top_matches function()
# e.g.
# movies = transform_prefs(critics)
# top_movies = top_matches(movies, 'Superman Returns')


# convert from user's based into item-based
def calculate_similar_items(prefs, n=10):
    result = {}
    item_prefs = transform_prefs(prefs)
    c = 0  # status
    for item in item_prefs:
        c += 1
        if c % 100 == 0:
            print('%d' % (c/len(item_prefs)))
        # most similar item to each other
        scores = top_matches(item_prefs, item, n=n)
        result[item] = scores
    return result
