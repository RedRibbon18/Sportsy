from framework.components.bet_slip import BetSlipComponent
from framework.components.match_list import MatchListComponent
from framework.components.toolbar import ToolbarComponent
from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage(BasePage):
    # Locators stored cleanly as class variables
    WAIT_ELEMENT = (By.ID, "match-list")

    def __init__(
        self,
        driver: WebDriver,
        base_url: str,
        test_id: str,
        user_id: str,
        page_time_out: int = 10,
    ):
        super().__init__(driver, test_id, page_time_out)
        self.url = f"{base_url}/?user-id={user_id}"
        self.toolbar = ToolbarComponent(
            driver, test_id=test_id
        )  # Initialize the Toolbar component
        self.match_list = MatchListComponent(
            driver, test_id=test_id
        )  # Initialize the Match List component
        self.bet_slip = BetSlipComponent(
            driver, test_id=test_id
        )  # Initialize the Bet Slip component

    def load(self):
        self.driver.get(self.url)
        self.wait_for_page_to_load()
        self.verify_page_loaded()

    def get_toolbar_title(self):
        """Get the title from the toolbar component"""
        return self.toolbar.get_title()

    def get_toolbar_balance(self):
        """Get the balance from the toolbar component"""
        return self.toolbar.get_balance()

    def get_match_list(self):
        """Get the match list component"""
        return self.match_list

    def get_bet_slip(self):
        """Get the bet slip component"""
        return self.bet_slip
