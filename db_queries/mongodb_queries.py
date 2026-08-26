"""MongoDB queries and collection validation helpers."""

from typing import Any, Dict, Optional
from utils.mongo_client import MongoDBClient
from config.settings import settings


class UserMongoQueries:
    """Encapsulates MongoDB Atlas queries for document-based user validation."""

    def __init__(self, mongo_client: MongoDBClient) -> None:
        self.client = mongo_client
        self.collection_name = settings.MONGODB_COLLECTION  # Default or {{MONGODB_COLLECTION}}

    def get_user_document(self, email: str) -> Optional[Dict[str, Any]]:
        query = {"email": email}
        return self.client.find_one(self.collection_name, query)

    def verify_user_activity_logged(self, user_id: str, action: str) -> bool:
        query = {"user_id": user_id, "action": action}
        result = self.client.find_one("audit_logs", query)
        return result is not None
