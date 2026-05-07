import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

# Training data
X = np.array([
    [7.0, 6.5, 2.0, 25, 2],
    [7.2, 6.0, 3.0, 26, 3],
    [6.5, 5.0, 5.0, 28, 5],
    [5.5, 3.0, 8.0, 30, 8],
    [8.5, 2.5, 9.0, 32, 9],
])

# Labels
Y = ["GOOD", "GOOD", "MODERATE", "UNSAFE", "UNSAFE"]

model = DecisionTreeClassifier()
model.fit(X, Y)

joblib.dump(model, "model.pkl")

print("Model Created Successfully")