from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X, y = load_boston(return_X_y=True)
train_features, test_features, train_labels, test_labels = train_test_split(X ,y ,random_state=0)
lr = LinearRegression().fit(train_features, train_labels)

training_score = lr.score(train_features, train_labels)
test_score = lr.score(test_features, test_labels)

print("Training set score: {:.2f}".format(training_score))
print("Test set score: {:.2f}".format(test_score))
