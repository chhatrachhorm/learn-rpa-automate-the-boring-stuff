from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
x = iris.data
y = iris.target
X_test, X_train, Y_test, Y_train = train_test_split(
    x, y, train_size=.5
)


def get_x_test():
    return X_test


def get_x_train():
    return X_train


def get_y_test():
    return Y_test


def get_y_train():
    return Y_train
