from sklearn import tree
from sklearn.metrics import accuracy_score
from SKL.mClassifiers import Data


tree_clf = tree.DecisionTreeClassifier()
tree_clf.fit(Data.X_train, Data.Y_train)
print(accuracy_score(Data.Y_test, tree_clf.predict(Data.X_test)))


