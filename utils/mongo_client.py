"""MongoDB Atlas client wrapper for document database validation."""

from typing import Any, Dict, List, Optional
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from config.settings import settings


class MongoDBClient:
    """Manages connections and queries against MongoDB Atlas."""

    def __init__(self) -> None:
        self.uri = settings.MONGODB_URI
        self.db_name = settings.MONGODB_DATABASE
        self.client: Optional[MongoClient] = None

    def connect(self) -> Optional[MongoClient]:
        if self.client is None:
            try:
                self.client = MongoClient(self.uri, serverSelectionTimeoutMS=2000)
            except Exception as e:
                print(f"[MongoDBClient Warning] Connection offline: {e}")
                self.client = None
        return self.client

    def get_database(self, name: Optional[str] = None) -> Optional[Database]:
        client = self.connect()
        if not client:
            return None
        return client[name or self.db_name]

    def get_collection(
        self, collection_name: str, db_name: Optional[str] = None
    ) -> Optional[Collection]:
        db = self.get_database(db_name)
        if db is None:
            return None
        return db[collection_name]

    def find_one(
        self, collection_name: str, query: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        try:
            collection = self.get_collection(collection_name)
            if collection is None:
                return None
            return collection.find_one(query)
        except Exception as e:
            print(f"[MongoDBClient Warning] Document lookup skipped: {e}")
            return None

    def find_many(
        self, collection_name: str, query: Dict[str, Any], limit: int = 10
    ) -> List[Dict[str, Any]]:
        try:
            collection = self.get_collection(collection_name)
            if collection is None:
                return []
            cursor = collection.find(query).limit(limit)
            return list(cursor)
        except Exception as e:
            print(f"[MongoDBClient Warning] Document search skipped: {e}")
            return []

    def close(self) -> None:
        if self.client:
            self.client.close()
            self.client = None
