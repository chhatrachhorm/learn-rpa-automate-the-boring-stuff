from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.RealtimeData.dataLoader import *
from CognitiveDecision.CollectiveIntelligence.CollaborativeFiltering.recommending import *
prefs = load_movieslen()
print('Value of 87', prefs['85'])

# user based recommendation
rec = get_recommendations(prefs, '87')[:3]
print(rec)