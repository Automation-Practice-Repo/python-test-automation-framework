"""Base page class with common page object methods."""
from typing import Optional, Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def wait_for_element(self, locator: Tuple[str, str], timeout: int = 30) -> Optional[object]:
        """Wait for element to be present."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            return None

    def wait_for_element_clickable(self, locator: Tuple[str, str], timeout: int = 30) -> Optional[object]:
        """Wait for element to be clickable."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            return None

    def wait_for_element_visible(self, locator: Tuple[str, str], timeout: int = 30) -> Optional[object]:
        """Wait for element to be visible."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            return None

    def click(self, locator: Tuple[str, str]) -> None:
        """Click on element."""
        element = self.wait_for_element_clickable(locator)
        if element:
            element.click()

    def enter_text(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """Enter text into element."""
        element = self.wait_for_element_visible(locator)
        if element:
            if clear_first:
                element.clear()
            element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Get text from element."""
        element = self.wait_for_element_visible(locator)
        return element.text if element else ""

    def is_element_visible(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is present in DOM."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_attribute(self, locator: Tuple[str, str], attribute: str) -> Optional[str]:
        """Get element attribute value."""
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute) if element else None

    def take_screenshot(self, name: str = "screenshot") -> str:
        """Take screenshot and return path."""
        import datetime
        filename = f"{name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        self.driver.save_screenshot(filename)
        return filename

    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Scroll to element."""
        element = self.wait_for_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def select_dropdown_by_value(self, locator: Tuple[str, str], value: str) -> None:
        """Select dropdown option by value."""
        from selenium.webdriver.support.ui import Select
        element = self.wait_for_element_visible(locator)
        if element:
            select = Select(element)
            select.select_by_value(value)

    def hover_over_element(self, locator: Tuple[str, str]) -> None:
        """Hover over element."""
        from selenium.webdriver.common.action_chains import ActionChains
        element = self.wait_for_element_visible(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
