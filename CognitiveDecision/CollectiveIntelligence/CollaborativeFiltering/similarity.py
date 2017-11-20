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
