"""Centralized locators for Home Page components using Playwright role and text conventions."""


class HomeLocators:
    """Locators for Home Page components."""

    HEADER_LOGO = "header a.logo, [aria-label*='Logo'], header a"
    NAV_LOGIN_BUTTON = "button:has-text('Sign In'), a:has-text('Login')"
    SEARCH_INPUT = "input[type='search'], input[name='q'], input[name='search'], input[placeholder*='search'], input[placeholder*='Search']"
    SEARCH_BUTTON = "button[type='submit'], button:has-text('Search')"
    HERO_BANNER = ".hero-banner, [data-testid='hero-banner']"
    FOOTER = "footer, [data-testid='footer']"
