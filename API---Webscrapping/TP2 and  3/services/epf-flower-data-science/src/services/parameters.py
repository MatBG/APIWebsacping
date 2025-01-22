import os
import json

PARAMETERS_FILE = "services/epf-flower-data-science/src/config/model_parameters.json"

def load_model_parameters() -> dict:
    """
    Load model parameters from the JSON configuration file.

    Returns:
        dict: Parameters dictionary.
    """
    if not os.path.exists(PARAMETERS_FILE):
        raise FileNotFoundError(f"Parameters file not found at {PARAMETERS_FILE}")
    
    with open(PARAMETERS_FILE, "r") as file:
        params = json.load(file)
    
    return params
