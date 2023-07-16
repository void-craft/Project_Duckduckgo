"""
This module has DuckDuckGoResultPage,
the page object for DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class ResultPage:

    RESULT_LINKS_CSS = (By.CSS_SELECTOR, "a.result__a")
    TEXTBOX_SEARCH_ID = (By.ID, "search_form_input")

    def __init__(self, browser):
        self.browser = browser

    def get_result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS_CSS)
        titles = [link.text for link in links]
        return titles

    def get_search_box_value(self):
        element = self.browser.find_element(*self.TEXTBOX_SEARCH_ID)
        value = element.get_attribute('value')
        return value

    def get_title(self):
        return self.browser.title
