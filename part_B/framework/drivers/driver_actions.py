from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, locator, log_id, timeout: int = 10):
    """Method to return an element on the page with a specified timeout.
    The element is located using the provided locator, which can be a tuple
    of (By, value).
    If an element is not found within the specified timeout, a
    TimeoutException is raised.
    The element does not need to be visible, just present in the DOM.
    """
    try:
        return WebDriverWait(driver, timeout=timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        print(f"The element: {locator} was not found within {timeout} seconds.")
        driver.save_screenshot(f"{log_id}_find_element_error.png")
        raise


def find_visible_elements(driver, locator, log_id, timeout: int = 10):
    """Method to return a list of elements on the page with a specified timeout.
    The elements are located using the provided locator, which can be a tuple
    of (By, value).
    If no elements are found within the specified timeout, a
    TimeoutException is raised.
    The elements need to be visible.
    """
    try:
        return WebDriverWait(driver, timeout=timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    except TimeoutException:
        print(f"The elements: {locator} were not visible within {timeout} seconds.")
        driver.save_screenshot(f"{log_id}_find_visible_elements_error.png")
        raise


def find_visible_element(driver, locator, log_id, timeout: int = 10):
    """Method to return an element on the page with a specified timeout.
    The element is located using the provided locator, which can be a tuple
    of (By, value).
    If an element is not found within the specified timeout, a
    TimeoutException is raised.
    The element needs to be visible.
    """
    try:
        return WebDriverWait(driver, timeout=timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        print(f"The element: {locator} was not visible within {timeout} seconds.")
        driver.save_screenshot(f"{log_id}find_visible_element_error.png")
        raise


def click(driver, locator, log_id, timeout: int = 10):
    """Method to click on an element on the page with a specified timeout.
    The element is located using the provided locator, which can be a tuple
    of (By, value).
    If an element is not found within the specified timeout, a
    TimeoutException is raised and a screenshot is taken.
    """
    try:
        element = WebDriverWait(driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    except TimeoutException:
        print(
            f"The element: {locator} did not become clickable within {timeout} seconds."
        )
        driver.save_screenshot(f"{log_id}_timeout_error.png")
        raise


def send_keys(driver, locator, text, log_id, timeout: int = 10):
    """Method to send keys to an element on the page with a specified timeout.
    The element is located using the provided locator, which can be a tuple
    of (By, value).
    If an element is not found within the specified timeout, a
    TimeoutException is raised.
    The element needs to be clickable before sending keys to avoid
    ElementNotInteractableException.
    """
    try:
        element = WebDriverWait(driver, timeout=timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.clear()
        element.send_keys(text)
    except TimeoutException:
        print(
            f"The element: {locator} did not become clickable within {timeout} seconds."
        )
        driver.save_screenshot(f"{log_id}_send_keys_error.png")
        raise


class DriverExplicitWaitActions():
    """
    Class to use explicit waits in selenium web driver, also includes
    taking screenshots of tiemout exceptions, saving files with "log_id" prefix
    """
    def __init__(self, driver, log_id):
        self.driver = driver
        self.log_id = log_id

    def find_element(self, locator, timeout: int = 10):
        return find_element(
            self.driver, locator, log_id=self.log_id, timeout=timeout
        )

    def find_visible_elements(self, locator, timeout: int = 10):
        return find_visible_elements(
            self.driver, locator, log_id=self.log_id, timeout=timeout
        )

    def find_visible_element(self, locator, timeout: int = 10):
        return find_visible_element(
            self.driver, locator, log_id=self.log_id, timeout=timeout
        )

    def click(self, locator, timeout: int = 10):
        click(
            self.driver, locator, log_id=self.log_id, timeout=timeout
        )

    def send_keys(self, locator, text, timeout: int = 10):
        send_keys(
            self.driver, locator, text, log_id=self.log_id, timeout=timeout
        )

