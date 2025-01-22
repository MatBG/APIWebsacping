import os
import opendatasets as od
from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, Query
from src.services.data import load_iris_dataset
from src.services.cleaning import process_iris_data
from src.services.data import split_iris_data
from src.services.training import train_model
from pydantic import BaseModel
from src.services.training import make_predictions


router = APIRouter()

DATASET_URL = "https://www.kaggle.com/datasets/uciml/iris"
DATA_FOLDER = "src/data"

@router.post("/download-dataset", summary="Download Kaggle Iris dataset")
async def download_dataset():
    """
    Downloads the Iris dataset from Kaggle and saves it to the src/data folder.
    """
    try:
        # Create the data directory if it doesn't exist
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)

        # Download the dataset using opendatasets
        od.download(DATASET_URL, DATA_FOLDER)
        return {"message": "Dataset downloaded successfully.", "path": DATA_FOLDER}
    except Exception as e:
        return {"error": str(e)}

@router.get("/load-dataset", summary="Load Iris dataset")
async def load_dataset():
    """
    Endpoint to load the Iris dataset file and return its content as JSON.
    """
    try:
        dataset = load_iris_dataset()
        return {"data": dataset}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/process-dataset", summary="Process Iris dataset")
async def process_dataset():
    """
    Endpoint to process the Iris dataset before training.
    """
    try:
        processed_data = process_iris_data()
        return {"processed_data": processed_data}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/split-dataset", summary="Split Iris dataset into train and test sets")
async def split_dataset(
    test_size: float = Query(0.2, ge=0.1, le=0.5, description="Proportion of test set (default is 20%)"),
    random_state: int = Query(42, description="Random seed for reproducibility")
):
    """
    Endpoint to split the Iris dataset into training and testing sets.
    """
    try:
        split_data = split_iris_data(test_size=test_size, random_state=random_state)
        return split_data
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/train-model", summary="Train classification model")
async def train_classification_model():
    print("POST /data/train-model endpoint reached.")
    try:
        model_path = train_model()
        return {"message": "Model trained and saved successfully.", "model_path": model_path}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@router.post("/predict", summary="Make predictions with the trained model")
async def predict(input_data: PredictionInput):
    print("POST /data/predict endpoint reached with data:", input_data)
    try:
        parameters = input_data.dict()
        predictions = make_predictions(parameters)
        return {"predictions": predictions}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

