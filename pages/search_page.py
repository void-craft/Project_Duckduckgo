"""
This module has DuckDuckGoSearchPage,
the page object for DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage:

    URL = "https://duckduckgo.com/"
    TEXTBOX_SEARCH_CSS = (By.CSS_SELECTOR, "#searchbox_input.searchbox_input__bEGm3")
    IMG_LOGO_CSS = (By.CSS_SELECTOR, ".legacy-homepage_logo__DLUJg")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_logo(self):
        element = self.browser.find_element(*self.IMG_LOGO_CSS)
        return element

    def search_phrase(self, phrase):
        textbox = self.browser.find_element(*self.TEXTBOX_SEARCH_CSS)
        textbox.send_keys(phrase + Keys.RETURN)
