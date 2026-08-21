"""Base Page Object wrapping Playwright Page operations."""

from typing import Optional
from playwright.sync_api import Page, Response, expect


class BasePage:
    """Base Page Object containing reusable UI interaction patterns."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> Optional[Response]:
        """Navigate to a specified URL using Playwright built-in synchronization."""
        return self.page.goto(url, wait_until="domcontentloaded")

    def get_title(self) -> str:
        """Get current page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Get current page URL."""
        return self.page.url

    def click(self, selector: str) -> None:
        """Click an element using auto-waiting."""
        self.page.click(selector)

    def fill(self, selector: str, value: str) -> None:
        """Fill an input field after clearing existing text."""
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        """Retrieve inner text of an element."""
        return self.page.inner_text(selector)

    def is_visible(self, selector: str, timeout: int = 1500) -> bool:
        """Check if an element is visible within a fast timeout window."""
        try:
            return self.page.is_visible(selector, timeout=timeout)
        except Exception:
            return False

    def assert_url_contains(self, expected_substring: str) -> None:
        """Assert current URL contains expected string using Playwright assertions."""
        expect(self.page).to_have_url(lambda url: expected_substring in url)
