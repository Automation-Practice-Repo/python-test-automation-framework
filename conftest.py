"""Root pytest configuration and shared fixtures."""

import os
from typing import Generator
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from utils.api_client import APIClient
from fixtures.db_fixtures import sql_client, mongo_client, sql_user_queries, mongo_user_queries


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    """Provide a session-scoped API Client fixture."""
    return APIClient()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    """Override Playwright browser context options if needed."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="function", autouse=True)
def print_test_name(request: pytest.FixtureRequest) -> Generator[None, None, None]:
    """Logs test execution start and completion."""
    print(f"\n[START] Executing test: {request.node.name}")
    yield
    print(f"\n[END] Completed test: {request.node.name}")
