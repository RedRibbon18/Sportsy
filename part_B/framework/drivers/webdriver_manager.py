from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverManager:
    def __init__(self, browser_name: str = "chrome", headless: bool = False):
        self.browser_name = browser_name.lower()
        self.headless = headless

    def get_driver(self):
        if self.browser_name == "firefox":
            return self._get_firefox_driver()
        return self._get_chrome_driver()

    def _get_chrome_driver(self):
        options = ChromeOptions()
        if self.headless:
            # Run without UI (ideal for CI/CD)
            options.add_argument("--headless=new")
            # Temporarily bypasses hardware rendering issues
            options.add_argument("--disable-gpu")
            # Ensures consistent responsive layouts
            options.add_argument("--window-size=1920,1080")

        # Start fresh without history or cache
        options.add_argument("--incognito")
        # Starts the browser window maximized
        options.add_argument("--start-maximized")
        # Overcomes limited resource issues
        options.add_argument("--disable-dev-shm-usage")
        # Fixes environment restriction issues
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def _get_firefox_driver(self):
        options = FirefoxOptions()
        if self.headless:
            options.headless = True
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        return driver
