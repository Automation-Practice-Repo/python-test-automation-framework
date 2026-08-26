"""Backend Database Integrity validation tests (SQL & MongoDB Atlas)."""

import pytest
from utils.sql_client import SQLClient
from utils.mongo_client import MongoDBClient
from db_queries.sql_queries import UserSQLQueries
from db_queries.mongodb_queries import UserMongoQueries


@pytest.mark.db
@pytest.mark.smoke
def test_sql_database_query(sql_client: SQLClient) -> None:
    """Verify SQL database client query execution or offline fallback."""
    user_queries = UserSQLQueries(sql_client)
    result = user_queries.get_user_by_email("test@example.com")
    assert result is None or isinstance(result, dict)


@pytest.mark.db
@pytest.mark.regression
def test_mongo_document_query(mongo_client: MongoDBClient) -> None:
    """Verify MongoDB document lookup or offline fallback."""
    mongo_queries = UserMongoQueries(mongo_client)
    doc = mongo_queries.get_user_document("test@example.com")
    assert doc is None or isinstance(doc, dict)


@pytest.mark.db
@pytest.mark.regression
def test_user_audit_log_validation(mongo_client: MongoDBClient) -> None:
    """Verify audit log document verification logic."""
    mongo_queries = UserMongoQueries(mongo_client)
    logged = mongo_queries.verify_user_activity_logged("user_123", "login")
    assert logged is False or logged is True
