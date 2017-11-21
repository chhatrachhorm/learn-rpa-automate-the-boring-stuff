from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering import recommendations

# ways to find similarity
# 1. Euclidean Distance Score
# 2. Pearson Correlation


# euclidean
pref = recommendations.sim_distance(
    recommendations.critics, 'Lisa Rose', 'Gene Seymour'
)
pref2 = recommendations.sim_distance(
    recommendations.critics, 'Lisa Rose', 'Michael Phillips'
)
pref3 = recommendations.sim_distance(
    recommendations.critics, 'Chhatra', 'Chhorm'
)
print(pref, pref2, pref3)

# correlation coefficient
pref4 = recommendations.sim_pearson(
    recommendations.critics, 'Lisa Rose', 'Gene Seymour'
)
print(pref4)


# ranking
rank = recommendations.top_matches(
    recommendations.critics, 'Toby', n=4
)
print(rank)

# recommendation
rec1 = recommendations.get_recommendations(
    recommendations.critics, 'Toby'
)
rec2 = recommendations.get_recommendations(
    recommendations.critics, 'Chhatra'
)
rec3 = recommendations.get_recommendations(
    recommendations.critics, 'Toby', recommendations.sim_distance
)
print('The recommendation: ')
print(rec1, rec2, rec3)