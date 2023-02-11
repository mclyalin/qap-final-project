from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from urllib.parse import urlparse


class BasePage(object):

    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def get(self, url):
        self._web_driver.get(url)
        # self.wait_page_loaded()

    def find_element(self, locator, timeout=10):
        """ Find element on the page. """

        return WebDriverWait(self._web_driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Not find {locator}")
