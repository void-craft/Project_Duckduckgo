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
    BUTTON_SEARCH_CSS = (By.CSS_SELECTOR, "button[aria-label='Search']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_logo(self):
        element = self.browser.find_element(*self.IMG_LOGO_CSS)
        return element

    def enter_search_item(self, phrase):
        textbox = self.browser.find_element(*self.TEXTBOX_SEARCH_CSS)
        textbox.send_keys(phrase)

    def click_search_button(self):
        element = self.browser.find_element(*self.BUTTON_SEARCH_CSS)
        element.click()

    def search_phrase(self, phrase):
        textbox = self.browser.find_element(*self.TEXTBOX_SEARCH_CSS)
        textbox.send_keys(phrase + Keys.RETURN)
