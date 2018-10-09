from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class LerningData:

    def __init__(self, neighbors, trainingAccuracy, testAccuracy):
        self.neighbors = neighbors
        self.trainingAccuracy = trainingAccuracy
        self.testAccuracy = testAccuracy

    def __str__(self):
        return "neighboars: {:2d},\t\t training accuracy: {:17.16f},\t\t test accuracy: {:17.16f}".format(self.neighbors, self.trainingAccuracy, self.testAccuracy)


cancer = load_breast_cancer()
train_features, test_features, train_labels, test_labels = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)

learning_data = []

for n_neighbors in range(1, 11):
    # build the model
    clf = KNeighborsClassifier(n_neighbors = n_neighbors)
    clf.fit(train_features, train_labels)

    # record training set accuracy
    training_accuracy = clf.score(train_features, train_labels)

    # record generalization accuracy
    test_accuracy = clf.score(test_features , test_labels)

    data = LerningData(n_neighbors, training_accuracy, test_accuracy)
    learning_data.append(data)

for data in learning_data:
    print(data)
