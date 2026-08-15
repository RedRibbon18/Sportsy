from framework.drivers.driver_actions import DriverExplicitWaitActions
from selenium.webdriver.remote.webdriver import WebDriver


class BaseComponent:
    """Represents the base component of the web application."""

    def __init__(self, driver: WebDriver, test_id):
        self.driver = driver
        self.test_id = test_id
        self.driver_explicit_wait = DriverExplicitWaitActions(self.driver, self.test_id)

