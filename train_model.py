from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import pickle

digits = load_digits()

X = digits.data
y = digits.target

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")