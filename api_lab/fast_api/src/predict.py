import joblib
import numpy as np

def predict_data(X):
    """
    Predict class label for the given input feature list.
    Args:
        X (List[List[float]]): A 2D list of wine features
    Returns:
        y_pred (int): Predicted class
    """
    model = joblib.load("../model/wine_model.pkl")
    y_pred = model.predict(np.array(X))
    return y_pred