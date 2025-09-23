import joblib
import numpy as np
import os

def predict_data(X):
    """
    Predict class label for the given input feature list.
    Args:
        X (List[List[float]]): A 2D list of wine features
    Returns:
        y_pred (int): Predicted class
    """
    model_path = os.path.join(os.path.dirname(__file__), "../model/wine_model.pkl")
    model_path = os.path.abspath(model_path)

    model = joblib.load(model_path)
    y_pred = model.predict(np.array(X))
    return y_pred