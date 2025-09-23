import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_data():
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target

    features = ['alcohol', 'malic_acid', 'alcalinity_of_ash',
                'flavanoids', 'nonflavanoid_phenols', 'color_intensity']
    
    X = df[features]
    y = df['target']
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
    return X_train, X_test, y_train, y_test