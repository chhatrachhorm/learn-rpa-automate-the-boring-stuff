from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.similarity import sim_pearson


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


# Item Based Filtering
# get recommendation based on the items similarity
# similarity here is based on user's rating
def get_recommendation_items(prefs, items, user):
    user_ratings = prefs[user]
    totals = {}
    ssum = {}

    # item rated by the user
    for (item, rating) in user_ratings.items():
        # loop over item similar to this one
        for(similarity, item2) in items[item]:
            if item2 in user_ratings:
                continue
            if similarity <= 0:
                continue
            totals.setdefault(item2, 0)
            totals[item2] += similarity * rating
            ssum.setdefault(item2, 0)
            ssum[item2] += similarity
    rankings = [(total/ssum[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
