from framework.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class MatchListComponent(BaseComponent):
    """Represents the match list component of the web application.
    It is responsible for displaying a list of match cards, each
    representing a specific match.
    """

    def __init__(self, driver: WebDriver, test_id: str):
        super().__init__(driver, test_id)
        # Locators for a match list card
        self._match_cards = (By.CLASS_NAME, "matchCard")
        # Locators for match meta data. Format = "TIME-BADGE League•Date"
        # with date format: "weekday, month day"
        # e.g: "UPCOMING Premier League•Sun, Sep 16"
        self._meta_data = (By.CLASS_NAME, "matchMeta")
        # a teamName spanfor each team
        self._team_names = (By.CLASS_NAME, "teamName")
        # Odds grid elements
        self._odds_value = (By.CLASS_NAME, "oddsButtonValue")

    def _get_card_id(self, card_element: WebElement):
        """Get the ID of a match card element."""
        return card_element.get_attribute("id")

    def _get_odds_button_locator(self, card_id: str, result: str):
        assert result in ["home", "draw", "away"], (
            "Result must be 'home', 'draw', or 'away'."
        )
        """Get the odds button element for a specific match and result."""
        # odds button format that we want: odds-serie-a-juve-milan-home
        # match card id format that we have (card_id): match-card-serie-a-juve-milan
        odds_id = card_id.replace("match-card-", "odds-")
        odds_id = f"{odds_id}-{result}"
        return (By.ID, odds_id)

    def click_odds_button(self, card_element: WebElement, result: str):
        """Click the odds button for a specific match and result."""
        card_id = self._get_card_id(card_element)
        odds_locator = self._get_odds_button_locator(card_id, result)
        self.driver_explicit_wait.click(odds_locator)

    def click_home_odds_button_for_card(self, card_element: WebElement):
        """Click the home odds button for a specific match card."""
        self.click_odds_button(card_element, "home")

    def click_draw_odds_button_for_card(self, card_element: WebElement):
        """Click the draw odds button for a specific match card."""
        self.click_odds_button(card_element, "draw")

    def click_away_odds_button_for_card(self, card_element: WebElement):
        """Click the away odds button for a specific match card."""
        self.click_odds_button(card_element, "away")

    def get_teams_names_for_card(self, card_element: WebElement):
        """Get the team names for a specific match card."""
        team_name_elements = card_element.find_elements(*self._team_names)
        return [team.text for team in team_name_elements]

    def get_card_meta_data(self, card_element: WebElement):
        """Get the meta data text from a specific match card."""
        return card_element.find_element(*self._meta_data).text

    def get_card_odds_for_result(self, card_element: WebElement, result: str):
        """Get the odds value for a specific match card and result."""
        card_id = self._get_card_id(card_element)
        odds_locator = self._get_odds_button_locator(card_id, result)
        odds_element = self.driver_explicit_wait.find_visible_element(odds_locator)
        return odds_element.find_element(*self._odds_value).text

    def select_card_by_index(self, index: int):
        """Select a match card by its index in the list."""
        match_cards = self.driver_explicit_wait.find_visible_elements(self._match_cards)
        if index < 0 or index >= len(match_cards):
            raise IndexError("Index out of range for match cards.")
        return match_cards[index]

    def select_cards_by_time_badge(self, time_badge: str):
        """Select match cards by their time badge text.
        The time badge is part of the match meta data, which is formatted as:
        "TIME-BADGE League•Date"
        TIME-BADGE can be "UPCOMING", "LIVE", or "PAST".
        """
        assert time_badge in ["UPCOMING", "LIVE", "PAST"], (
            "Time badge must be 'UPCOMING', 'LIVE', or 'PAST'."
        )
        match_cards = self.driver_explicit_wait.find_visible_elements(self._match_cards)
        selected_cards = []
        for card in match_cards:
            meta_data = self.get_card_meta_data(card)
            if time_badge in meta_data:
                selected_cards.append(card)
        return selected_cards

    def select_first_card_by_time_badge(self, time_badge: str):
        assert time_badge in ["UPCOMING", "LIVE", "PAST"], (
            "Time badge must be 'UPCOMING', 'LIVE', or 'PAST'."
        )
        match_cards = self.driver_explicit_wait.find_visible_elements(self._match_cards)
        for card in match_cards:
            meta_data = self.get_card_meta_data(card)
            if time_badge in meta_data:
                return card  # Return the first match card that matches the time badge
        return None
