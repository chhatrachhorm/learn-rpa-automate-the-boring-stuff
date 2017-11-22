from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.similarity import *
from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.critics import *
from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.ranking import *
from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.recommending import *
# ways to find similarity
# 1. Euclidean Distance Score
# 2. Pearson Correlation
# euclidean
pref = sim_distance(
    critics, 'Lisa Rose', 'Gene Seymour'
)
pref2 = sim_distance(
    critics, 'Lisa Rose', 'Michael Phillips'
)
pref3 = sim_distance(
    critics, 'Chhatra', 'Chhorm'
)
print(pref, pref2, pref3)

# correlation coefficient
pref4 = sim_pearson(
    critics, 'Lisa Rose', 'Gene Seymour'
)
print(pref4)


# ranking
rank = top_matches(
    critics, 'Toby', n=4
)
print(rank)

# recommendation
rec1 = get_recommendations(
    critics, 'Toby'
)
rec2 = get_recommendations(
    critics, 'Chhatra'
)
rec3 = get_recommendations(
    critics, 'Toby', sim_distance
)
print('The recommendation: ')
print(rec1, rec2, rec3)


# top match based on the user
# user who like A also like B, C, D
match = top_matches(
    transform_prefs(critics),
    'Superman Returns'
)
print('User who likes Superman returns also like', match)

# Item Based Filtering
# pre-computed item
itemSim = calculate_similar_items(critics)
print(itemSim)

rank = get_recommendation_items(critics, itemSim, 'Toby')
print('Item Based Recommendation', rank)
