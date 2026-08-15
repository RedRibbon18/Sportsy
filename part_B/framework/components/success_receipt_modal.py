from framework.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SuccessReceiptModal(BaseComponent):
    """Represents the success receipt modal of the web application."""

    def __init__(self, driver: WebDriver, test_id: str):
        super().__init__(driver, test_id)
        # Locators for the success modal container
        self._container = (By.ID, "modal-success")
        self._title = (By.CLASS_NAME, "modalTitle")
        self._close_x_button = (By.ID, "modal-success-close-x")
        self._close_button = (By.ID, "modal-success-close")
        self._bet_id = (By.ID, "modal-success-bet-id")
        self._match_info = (By.ID, "modal-success-match")
        self._stake = (By.ID, "modal-success-stake")
        self._odds = (By.ID, "modal-success-odds")
        self._payout = (By.ID, "modal-success-payout")
        self._placed_at = (By.ID, "modal-success-placed-at")

    def wait_for_modal(self, timeout: int = 10):
        """Wait for the success modal to appear."""
        self.driver_explicit_wait.find_visible_element(self._container, timeout=timeout)

    def get_modal_title(self):
        """Get the title text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._title).text

    def get_bet_id(self):
        """Get the bet ID text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._bet_id).text

    def get_match_info(self):
        """Get the match info text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._match_info).text

    def get_stake(self):
        """Get the bet stake info text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._stake).text

    def get_odds(self):
        """Get the bet odds info text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._odds).text

    def get_payout(self):
        """Get the bet potential payout info text from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._payout).text

    def get_timestamp(self):
        """Get the bet timestamp from the success modal."""
        return self.driver_explicit_wait.find_visible_element(self._placed_at).text

    def close_modal(self):
        """Close the success modal."""
        self.driver_explicit_wait.click(self._close_button)
