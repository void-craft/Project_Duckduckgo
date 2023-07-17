"""
This module has DuckDuckGoResultPage,
the page object for DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class ResultPage:

    LINK_RESULT_TITLES_CSS = (By.CSS_SELECTOR, "span[class$='EKtkFWMYpwzMKOYr0GYm.LQVY1Jpkk8nyJ6HBWKAk']")
    TEXTBOX_SEARCH_ID = (By.ID, "search_form_input")
    LINK_RESULT_CSS = (By.CSS_SELECTOR, ".eVNpHGjtxRBq_gLOfGDr.LQNqh2U1kzYxREs65IJu")
    BUTTON_MORE_ID = (By.ID, "more-results")

    def __init__(self, browser):
        self.browser = browser

    def get_result_link_titles(self):
        elements = self.browser.find_elements(*self.LINK_RESULT_TITLES_CSS)
        titles = [element.text for element in elements]
        return titles

    def get_search_box_value(self):
        element = self.browser.find_element(*self.TEXTBOX_SEARCH_ID)
        value = element.get_attribute('value')
        return value

    def get_title(self):
        return self.browser.title

    def load_result_page(self, search_term):
        url = f"https://duckduckgo.com/?va=v&t=ha&q={search_term}&ia=web"
        self.browser.get(url)

    def click_first_result_link(self):
        element = self.browser.find_element(*self.LINK_RESULT_CSS)
        element.click()

    def find_result_count(self):
        elements = self.browser.find_elements(*self.LINK_RESULT_CSS)
        count = len(elements)
        return count

    def click_more_results_link(self):
        element = self.browser.find_element(*self.BUTTON_MORE_ID)
        element.click()
