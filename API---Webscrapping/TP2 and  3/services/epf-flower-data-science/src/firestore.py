import google.auth
from google.cloud import firestore
from google.cloud import firestore
import os

class FirestoreClient:
    def init(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/serviceAccountKey.json"
        self.client = firestore.Client()

        
class FirestoreClient:
   """Wrapper around a database"""

   client: firestore.Client

   def __init__(self):
       """Initialize FirestoreClient"""
       self.client = None

   def init(self) -> None:
       """Init the client."""
       credentials, _ = google.auth.default() 
       self.client = firestore.Client(credentials=credentials)

   def get(self, collection_name: str, document_id: str) -> dict:
       """Find one document by ID."""
       doc = self.client.collection(collection_name).document(document_id).get()
       if doc.exists:
           return doc.to_dict()
       raise FileExistsError(f"No document found at {collection_name}/{document_id}")

   def get_parameters(self):
       """Get parameters from Firestore."""
       parameters_ref = self.client.collection('parameters').document('parameters')
       doc = parameters_ref.get()
       if doc.exists:
           return doc.to_dict()
       return self.create_parameters_document()

   def create_parameters_document(self):
       """Create parameters document in Firestore."""
       parameters_ref = self.client.collection('parameters').document('parameters')
       parameters_data = {
           'n_estimators': 100,
           'criterion': 'gini'
       }
       parameters_ref.set(parameters_data)
       return parameters_data