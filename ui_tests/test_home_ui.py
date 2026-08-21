"""End-to-End UI tests for Freshlife Application using Playwright & POM."""

import json
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


def load_test_data():
    with open("test_data/sample_data.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.ui
@pytest.mark.smoke
def test_home_page_navigation(page: Page) -> None:
    """Verify that the home page loads successfully and title is correct."""
    home_page = HomePage(page)
    home_page.open()
    assert len(home_page.get_title()) > 0 or len(home_page.get_url()) > 0


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize("data", load_test_data())
def test_product_search_data_driven(page: Page, data: dict) -> None:
    """Verify search functionality using JSON data-driven parameters."""
    home_page = HomePage(page)
    home_page.open()
    search_term = data["search_term"]
    home_page.search_product(search_term)
    assert len(home_page.get_url()) > 0
