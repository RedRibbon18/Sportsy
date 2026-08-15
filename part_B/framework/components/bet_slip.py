from framework.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BetSlipComponent(BaseComponent):
    """Represents the bet slip component of the web application."""

    def __init__(self, driver: WebDriver, test_id: str):
        super().__init__(driver, test_id)
        # Locators for the bet slip component
        self._container = (By.ID, "bet-slip")

        # header elements
        self._header = (By.ID, "bet-slip-header")
        self._title = (By.ID, "bet-slip-title")
        self.bet_count = (By.ID, "bet-slip-count")
        self._header_balance = (By.ID, "bet-slip-balance")
        # only prensent when there are selections in the bet slip
        self._remove_all = (By.ID, "bet-slip-remove-all")

        # Contents elements
        # only present when there are no selections in the bet slip
        self._empty = (By.CLASS_NAME, "betSlipBodyEmpty")
        # only present when there are selections in the bet slip
        # selection elements
        self._selection_teams = (By.CLASS_NAME, "betSelectionTeams")
        self._selection_market = (By.CLASS_NAME, "betSelectionMarket")
        self._selection_remove_button = (By.ID, "bet-slip-selection-remove")
        self._selection_odds = (By.CLASS_NAME, "betSelectionOdds")
        # Stake
        self._stake_input = (By.ID, "bet-slip-stake-input")

        # footer elements
        self._total_stake = (By.ID, "bet-slip-total-stake")
        self._potential_payout = (By.ID, "bet-slip-potential-payout")
        self._place_bet_button = (By.ID, "bet-slip-place-bet")

    def get_title(self):
        """Get the title text from the Bet Slip box."""
        return self.driver_explicit_wait.find_visible_element(self._title).text

    def get_balance(self):
        """Get the balance text from the Bet Slip header"""
        return self.driver_explicit_wait.find_visible_element(self._header_balance).text

    def get_selection_teams(self):
        """Get the selection teams element from the Bet Slip."""
        return self.driver_explicit_wait.find_visible_element(self._selection_teams).text

    def get_selection_market(self):
        """Get the selection market element from the Bet Slip."""
        return self.driver_explicit_wait.find_visible_element(self._selection_market).text

    def get_selection_odds(self):
        """Get the selection odds element from the Bet Slip."""
        return self.driver_explicit_wait.find_visible_element(self._selection_odds).text

    def get_total_stake(self):
        """Get the total stake element from the Bet Slip."""
        return self.driver_explicit_wait.find_visible_element(self._total_stake).text

    def get_potential_payout(self):
        """Get the potential payout element from the Bet Slip."""
        return self.driver_explicit_wait.find_visible_element(self._potential_payout).text

    def enter_stake(self, stake_value: str):
        """Set the stake value in the Bet Slip."""
        self.driver_explicit_wait.send_keys(self._stake_input, stake_value)

    def click_place_bet(self):
        """Click the place bet button in the Bet Slip."""
        self.driver_explicit_wait.click(self._place_bet_button)
