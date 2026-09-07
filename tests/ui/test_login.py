"""Sample UI test demonstrating Page Object Model."""
import pytest
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage


@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:
    """Login functionality tests."""

    def test_successful_login(self, chrome_driver):
        """Test successful login with valid credentials."""
        login_page = LoginPage(chrome_driver)
        login_page.navigate_to_login()
        login_page.login("admin@test.com", "Test@123")

        dashboard = DashboardPage(chrome_driver)
        assert dashboard.is_user_logged_in(), "User should be logged in"
        assert dashboard.get_page_title() == "Dashboard"

    def test_failed_login_wrong_password(self, chrome_driver):
        """Test login failure with wrong password."""
        login_page = LoginPage(chrome_driver)
        login_page.navigate_to_login()
        login_page.login("admin@test.com", "wrongpassword")

        assert login_page.is_error_displayed(), "Error should be displayed"
        assert "Invalid credentials" in login_page.get_error_message()

    def test_logout(self, chrome_driver):
        """Test user logout functionality."""
        login_page = LoginPage(chrome_driver)
        login_page.navigate_to_login()
        login_page.login("admin@test.com", "Test@123")

        dashboard = DashboardPage(chrome_driver)
        dashboard.logout()

        assert login_page.is_login_page_displayed(), "Should be on login page"
