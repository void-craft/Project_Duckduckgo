"""
These tests cover DuckDuckGo searches using search button.
"""

from pages.search_page import SearchPage
from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase', ['pink', 'green', 'yellow'])
def test_search_by_button_click(browser, phrase):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)

    # Given the DuckDuckGo homepage is displayed
    search_page.load()
    assert search_page.get_logo() is not None

    # When the user searches for a phrase by clicking search button
    search_page.enter_search_item(phrase)
    search_page.click_search_button()

    # Then the search result query is the phrase
    assert phrase == result_page.get_search_box_value()

    # And the search result links pertain to the phrase
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()

    # Then the search result title contains the phrase
    assert phrase in result_page.get_title()
