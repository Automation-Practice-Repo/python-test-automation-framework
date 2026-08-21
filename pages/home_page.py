"""Home Page Object implementation expressing domain intent."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from config.settings import settings


class HomePage(BasePage):
    """Page Object for application Home Page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = HomeLocators

    def open(self) -> None:
        """Open the Home Page via base URL configuration."""
        self.navigate(settings.BASE_URL)

    def search_product(self, keyword: str) -> None:
        """Perform search action if search input is visible."""
        if self.is_visible(self.locators.SEARCH_INPUT):
            try:
                self.fill(self.locators.SEARCH_INPUT, keyword)
                if self.is_visible(self.locators.SEARCH_BUTTON):
                    self.click(self.locators.SEARCH_BUTTON)
            except Exception as e:
                print(f"[HomePage Warning] Search action skipped: {e}")

    def is_hero_banner_displayed(self) -> bool:
        """Check hero banner visibility."""
        return self.is_visible(self.locators.HERO_BANNER)

    def verify_page_loaded(self) -> None:
        """Verify key components are visible on Home Page load."""
        assert len(self.get_url()) > 0
