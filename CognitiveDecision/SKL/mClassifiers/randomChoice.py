import random
from SKL.mClassifiers import Data
from sklearn.metrics import accuracy_score

class RandomClassifier():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predicts = []
        for _ in x_test:
            label = random.choice(self.y_train)
            predicts.append(label)
        return predicts


scrappy = RandomClassifier()
scrappy.fit(Data.X_train,Data.Y_train)
print(accuracy_score(Data.Y_test, scrappy.predict(Data.X_test)))
