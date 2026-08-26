"""SQL Database client wrapper for database validation."""

from typing import Any, List, Dict, Tuple, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from config.settings import settings


class SQLClient:
    """Manages connections and parameterized query executions for SQL databases."""

    def __init__(self) -> None:
        self.host = settings.DB_HOST
        self.port = settings.DB_PORT
        self.dbname = settings.DB_NAME
        self.user = settings.DB_USER
        self.password = settings.DB_PASSWORD
        self._connection = None

    def connect(self) -> Any:
        if not self._connection or getattr(self._connection, 'closed', True):
            try:
                self._connection = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    connect_timeout=3
                )
            except Exception as e:
                print(f"[SQLClient Warning] Database connection offline: {e}")
                self._connection = None
        return self._connection

    def execute_query(
        self, query: str, params: Optional[Tuple[Any, ...]] = None
    ) -> List[Dict[str, Any]]:
        conn = self.connect()
        if not conn:
            return []
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params or ())
                results = cursor.fetchall()
                return [dict(row) for row in results]
        except Exception as e:
            print(f"[SQLClient Warning] Query execution skipped: {e}")
            return []

    def execute_non_query(
        self, query: str, params: Optional[Tuple[Any, ...]] = None
    ) -> int:
        conn = self.connect()
        if not conn:
            return 0
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()
                return cursor.rowcount
        except Exception as e:
            print(f"[SQLClient Warning] Non-query execution skipped: {e}")
            return 0

    def close(self) -> None:
        if self._connection and not getattr(self._connection, 'closed', True):
            try:
                self._connection.close()
            except Exception:
                pass
        self._connection = None
