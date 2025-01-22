import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

DATASET_FILE = "src/data/Iris.csv"

def process_iris_data() -> dict:
    """
    Process the Iris dataset for training.
    """
    if not os.path.exists(DATASET_FILE):
        raise FileNotFoundError(f"Dataset file not found at {DATASET_FILE}")
    
    try:
        # Charger le dataset
        df = pd.read_csv(DATASET_FILE)
        print("Colonnes disponibles :", df.columns)

        # Renommer les colonnes pour uniformiser
        df.rename(columns={
            "SepalLengthCm": "sepal_length",
            "SepalWidthCm": "sepal_width",
            "PetalLengthCm": "petal_length",
            "PetalWidthCm": "petal_width",
            "Species": "species"
        }, inplace=True)

        # Vérifiez si la colonne "species" est présente
        if "species" not in df.columns:
            raise KeyError(f"'species' column not found in dataset. Columns available: {df.columns.tolist()}")

        # Procéder au traitement comme prévu
        label_encoder = LabelEncoder()
        df['species'] = label_encoder.fit_transform(df['species'])

        features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        scaler = StandardScaler()
        df[features] = scaler.fit_transform(df[features])
        
        return df.to_dict(orient="records")
    except Exception as e:
        print("Erreur lors du traitement :", e)
        raise
