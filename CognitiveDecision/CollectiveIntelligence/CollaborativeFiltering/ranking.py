from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.similarity import sim_pearson


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
