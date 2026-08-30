"""Centralized framework settings loaded from environment variables."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()


class Settings:
    """Application and test settings singleton."""

    BASE_URL: str = os.getenv("BASE_URL", "https://example.com")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "qa")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://reqres.in/api")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "30000"))

    # API Credentials
    API_KEY: Optional[str] = os.getenv("API_KEY", None)
    BEARER_TOKEN: Optional[str] = os.getenv("BEARER_TOKEN", None)

    # SQL Database Settings
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "freshlife_qa")
    DB_USER: str = os.getenv("DB_USER", "qa_user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "qa_password_placeholder")

    # MongoDB Atlas Settings
    MONGODB_URI: str = os.getenv(
        "MONGODB_URI",
        "mongodb+srv://<username>:<password>@cluster0.example.mongodb.net/?retryWrites=true&w=majority",
    )
    MONGODB_DATABASE: str = os.getenv("MONGODB_DATABASE", "freshlife_db")
    MONGODB_COLLECTION: str = os.getenv("MONGODB_COLLECTION", "users")


settings = Settings()
