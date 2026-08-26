"""Database fixtures for Pytest test runs."""

from typing import Generator
import pytest
from utils.sql_client import SQLClient
from utils.mongo_client import MongoDBClient
from db_queries.sql_queries import UserSQLQueries
from db_queries.mongodb_queries import UserMongoQueries


@pytest.fixture(scope="session")
def sql_client() -> Generator[SQLClient, None, None]:
    """Provide a session-scoped SQL database client."""
    client = SQLClient()
    yield client
    client.close()


@pytest.fixture(scope="session")
def mongo_client() -> Generator[MongoDBClient, None, None]:
    """Provide a session-scoped MongoDB Atlas client."""
    client = MongoDBClient()
    yield client
    client.close()


@pytest.fixture(scope="function")
def sql_user_queries(sql_client: SQLClient) -> UserSQLQueries:
    """Provide SQL User Queries query object for backend validation."""
    return UserSQLQueries(sql_client)


@pytest.fixture(scope="function")
def mongo_user_queries(mongo_client: MongoDBClient) -> UserMongoQueries:
    """Provide Mongo User Queries query object for document validation."""
    return UserMongoQueries(mongo_client)
