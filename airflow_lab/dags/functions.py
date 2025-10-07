import joblib
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Function to load data
def load_data():
    # Load the Breast Cancer dataset from scikit-learn
    cancer_data = load_breast_cancer()
    
    # Convert it to a pandas DataFrame
    df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
    
    # Add the target column
    df['target'] = cancer_data.target

    # Features and target
    X = df.drop('target', axis=1)  # Features (all except the target)
    y = df['target']  # Target (benign or malignant)

    # Convert X and y to lists or arrays before pushing to XCom
    X_list = X.values.tolist()  # Convert features to list
    y_list = y.tolist()  # Convert target to list

    return X_list, y_list

# Function to split data
def split_data(X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
    return X_train, X_test, y_train, y_test

# Function to train the model
def fit_model(X_train, y_train):
    print("Training model...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model as a pickle file
    model_path = '/opt/airflow/dags/model/cancer_model.pkl'
    joblib.dump(model, model_path)
    return model_path

# Function to make predictions
def predict_data(X):
    model_path = '/opt/airflow/dags/model/cancer_model.pkl'
    model = joblib.load(model_path)
    y_pred = model.predict(np.array(X))
    return y_pred
