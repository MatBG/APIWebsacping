from fastapi import APIRouter, HTTPException
from src.schemas.message import ParametersResponse
from src.firestore import FirestoreClient  # Import mis à jour

router = APIRouter(prefix="/api/v1")
firestore_client = FirestoreClient()
firestore_client.init()

@router.get("/parameters", response_model=ParametersResponse)
async def get_model_parameters():
    try:
        parameters = firestore_client.get_parameters()
        return parameters
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))