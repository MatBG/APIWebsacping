import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from src.services.parameters import load_model_parameters

DATASET_FILE = "src/data/Iris.csv"
MODEL_FOLDER = "src/models"
MODEL_FILE = os.path.join(MODEL_FOLDER, "iris_classifier.pkl")
MODEL_FILE = "src/models/iris_classifier.pkl"

def train_model() -> str:
    """
    Train a classification model on the processed Iris dataset and save it.
    
    Returns:
        str: Path to the saved model file.
    """
    if not os.path.exists(DATASET_FILE):
        raise FileNotFoundError(f"Dataset file not found at {DATASET_FILE}")

    # Load and preprocess the dataset
    df = pd.read_csv(DATASET_FILE)
    df.rename(columns={
        "SepalLengthCm": "sepal_length",
        "SepalWidthCm": "sepal_width",
        "PetalLengthCm": "petal_length",
        "PetalWidthCm": "petal_width",
        "Species": "species"
    }, inplace=True)
    
    # Encode target column
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    df['species'] = label_encoder.fit_transform(df['species'])

    # Split data into features and target
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[features]
    y = df['species']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load model parameters
    params = load_model_parameters()
    model_params = params["parameters"]

    # Initialize the model
    model = RandomForestClassifier(**model_params)

    # Train the model
    model.fit(X_train, y_train)
    
    # Create the models directory if it doesn't exist
    os.makedirs(MODEL_FOLDER, exist_ok=True)
    
    # Save the trained model
    with open(MODEL_FILE, "wb") as file:
        pickle.dump(model, file)

    return MODEL_FILE

def load_trained_model():
    """
    Load the trained model from the saved file.
    Returns:
        Trained model object.
    """
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(f"Trained model file not found at {MODEL_FILE}")

    with open(MODEL_FILE, "rb") as file:
        model = pickle.load(file)
    return model

def make_predictions(parameters: dict) -> list:
    """
    Make predictions with the trained model.
    Args:
        parameters: A dictionary containing feature values for prediction.
    Returns:
        List of predictions.
    """
    model = load_trained_model()
    input_data = np.array([[
        parameters["sepal_length"],
        parameters["sepal_width"],
        parameters["petal_length"],
        parameters["petal_width"]
    ]])
    predictions = model.predict(input_data)
    return predictions.tolist()