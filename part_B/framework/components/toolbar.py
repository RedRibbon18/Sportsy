from framework.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ToolbarComponent(BaseComponent):
    """Represents the tool bar component of the web application."""

    def __init__(self, driver: WebDriver, test_id: str):
        super().__init__(driver, test_id)
        # Locators for the toolbar component
        self._title = (By.ID, "header-title")
        self._balance = (By.ID, "header-balance")
        self._avatar = (By.ID, "header-avatar")

    def get_title(self):
        """Get the title text from the toolbar."""
        return self.driver_explicit_wait.find_visible_element(self._title).text

    def get_balance(self):
        """Get the balance text from the toolbar."""
        return self.driver_explicit_wait.find_visible_element(self._balance).text

    def get_avatar(self):
        """Get the avatar element from the toolbar."""
        return self.driver_explicit_wait.find_visible_element(self._avatar)
