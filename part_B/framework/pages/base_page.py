from framework.drivers.driver_actions import DriverExplicitWaitActions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver: WebDriver, test_id, page_time_out: int = 10):
        self.driver = driver
        self.test_id = test_id
        self.driver.set_page_load_timeout(page_time_out)
        self.driver_explicit_wait = DriverExplicitWaitActions(self.driver, self.test_id)

    def wait_for_page_to_load(self, timeout: int = 10):
        """Wait for the page to load completely by checking the document.readyState."""
        try:
            WebDriverWait(self.driver, timeout=timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            print(f"The page did not load within {timeout} seconds.")
            self.driver.save_screenshot(f"{self.test_id}_page_load_error.png")
            raise

    def verify_page_loaded(self):
        try:
            self.driver_explicit_wait.find_element(self.WAIT_ELEMENT, timeout=1)
        except TimeoutException:
            print(
                f"Couldn't verify page loaded successfully, missing element: {self.WAIT_ELEMENT}"
            )
            self.driver.save_screenshot(f"{self.test_id}_page_load_error.png")
            raise
