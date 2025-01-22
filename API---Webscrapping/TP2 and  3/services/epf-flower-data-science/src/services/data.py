from sklearn.model_selection import train_test_split
import pandas as pd
import os

DATASET_FILE = "src/data/Iris.csv"

def load_iris_dataset() -> list:
    """
    Load the Iris dataset from the local CSV file and return it as a list of dictionaries.
    
    Returns:
        List of rows as dictionaries (DataFrame converted to JSON format).
    """
    if not os.path.exists(DATASET_FILE):
        raise FileNotFoundError(f"Dataset file not found at {DATASET_FILE}")

    # Load the dataset
    df = pd.read_csv(DATASET_FILE)
    # Convert DataFrame to JSON-like structure (list of dicts)
    return df.to_dict(orient="records")

def split_iris_data(test_size: float = 0.2, random_state: int = 42) -> dict:
    """
    Split the Iris dataset into training and testing sets.
    
    Args:
        test_size: Proportion of the dataset to include in the test split (default is 20%).
        random_state: Random seed for reproducibility.

    Returns:
        A dictionary with training and testing sets.
    """
    DATASET_FILE = "src/data/Iris.csv"
    
    if not os.path.exists(DATASET_FILE):
        raise FileNotFoundError(f"Dataset file not found at {DATASET_FILE}")
    
    # Load the dataset
    df = pd.read_csv(DATASET_FILE)
    
    # Rename columns to match processing
    df.rename(columns={
        "SepalLengthCm": "sepal_length",
        "SepalWidthCm": "sepal_width",
        "PetalLengthCm": "petal_length",
        "PetalWidthCm": "petal_width",
        "Species": "species"
    }, inplace=True)
    
    # Encode the target column
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    df['species'] = label_encoder.fit_transform(df['species'])

    # Split into features (X) and target (y)
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[features]
    y = df['species']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Combine X and y back into DataFrames for returning
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)
    
    # Return as JSON-like dictionaries
    return {
        "train": train_data.to_dict(orient="records"),
        "test": test_data.to_dict(orient="records")
    }
