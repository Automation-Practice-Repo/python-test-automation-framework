"""SQL Queries and backend assertion helpers."""

from typing import Any, Dict, List, Optional
from utils.sql_client import SQLClient


class UserSQLQueries:
    """Encapsulates parameterized SQL queries for user entity validation."""

    def __init__(self, sql_client: SQLClient) -> None:
        self.client = sql_client

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        # Target table placeholder: {{SQL_TABLE}}
        query = "SELECT id, email, name, status, created_at FROM {{SQL_TABLE}} WHERE email = %s;"
        results = self.client.execute_query(query, (email,))
        return results[0] if results else None

    def get_user_order_count(self, user_id: str) -> int:
        query = "SELECT COUNT(*) as total FROM orders WHERE user_id = %s;"
        results = self.client.execute_query(query, (user_id,))
        return results[0]["total"] if results else 0
