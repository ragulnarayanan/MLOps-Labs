from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from data import load_data, split_data

def fit_model(X_train, y_train):
    print("Training model...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, '../model/wine_model.pkl')

print("Script is starting...")
if __name__ == "__main__":
    print("Loading data...")
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train)

