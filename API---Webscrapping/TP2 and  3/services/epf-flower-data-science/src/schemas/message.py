from src.schemas.camelcase import CamelCase

class ParametersResponse(CamelCase):
    n_estimators: int
    criterion: str