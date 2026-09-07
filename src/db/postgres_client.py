"""PostgreSQL client for database testing."""
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Optional, Any
import logging

logger = logging.getLogger(__name__)


class PostgresClient:
    """PostgreSQL database client for test validation."""

    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self) -> None:
        """Establish database connection."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
            logger.info(f"Connected to PostgreSQL: {self.host}/{self.database}")
        except psycopg2.Error as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def execute_query(self, query: str, params: Optional[tuple] = None) -> List[Dict]:
        """Execute SELECT query and return results."""
        try:
            self.cursor.execute(query, params)
            results = self.cursor.fetchall()
            return [dict(row) for row in results]
        except psycopg2.Error as e:
            logger.error(f"Query execution failed: {e}")
            raise

    def execute_update(self, query: str, params: Optional[tuple] = None) -> int:
        """Execute INSERT/UPDATE/DELETE and return row count."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.rowcount
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Update execution failed: {e}")
            raise

    def get_row(self, table: str, conditions: Dict[str, Any]) -> Optional[Dict]:
        """Get single row from table with WHERE conditions."""
        where_clause = " AND ".join([f"{k} = %s" for k in conditions.keys()])
        query = f"SELECT * FROM {table} WHERE {where_clause} LIMIT 1"
        self.cursor.execute(query, tuple(conditions.values()))
        result = self.cursor.fetchone()
        return dict(result) if result else None

    def get_table_data(self, table: str, limit: int = 100) -> List[Dict]:
        """Get all rows from table."""
        query = f"SELECT * FROM {table} LIMIT %s"
        self.cursor.execute(query, (limit,))
        return [dict(row) for row in self.cursor.fetchall()]

    def insert_row(self, table: str, data: Dict[str, Any]) -> int:
        """Insert row into table."""
        columns = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()
        return self.cursor.rowcount

    def update_rows(self, table: str, data: Dict[str, Any], conditions: Dict[str, Any]) -> int:
        """Update rows in table."""
        set_clause = ", ".join([f"{k} = %s" for k in data.keys()])
        where_clause = " AND ".join([f"{k} = %s" for k in conditions.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.cursor.execute(query, tuple(list(data.values()) + list(conditions.values())))
        self.connection.commit()
        return self.cursor.rowcount

    def delete_rows(self, table: str, conditions: Dict[str, Any]) -> int:
        """Delete rows from table."""
        where_clause = " AND ".join([f"{k} = %s" for k in conditions.keys()])
        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.cursor.execute(query, tuple(conditions.values()))
        self.connection.commit()
        return self.cursor.rowcount

    def row_exists(self, table: str, conditions: Dict[str, Any]) -> bool:
        """Check if row exists in table."""
        where_clause = " AND ".join([f"{k} = %s" for k in conditions.keys()])
        query = f"SELECT 1 FROM {table} WHERE {where_clause} LIMIT 1"
        self.cursor.execute(query, tuple(conditions.values()))
        return self.cursor.fetchone() is not None

    def get_count(self, table: str, conditions: Optional[Dict[str, Any]] = None) -> int:
        """Get row count from table."""
        if conditions:
            where_clause = " AND ".join([f"{k} = %s" for k in conditions.keys()])
            query = f"SELECT COUNT(*) FROM {table} WHERE {where_clause}"
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            query = f"SELECT COUNT(*) FROM {table}"
            self.cursor.execute(query)
        return self.cursor.fetchone()["count"]

    def close(self) -> None:
        """Close database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            logger.info("PostgreSQL connection closed")
