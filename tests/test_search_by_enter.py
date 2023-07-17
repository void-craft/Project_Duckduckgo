"""
This tests cover DuckDuckGo searches using enter key.
"""

from pages.search_page import SearchPage
from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase', ['lion', 'tiger', 'panda'])
def test_search_by_enter(browser, phrase):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)

    # Given the DuckDuckGo homepage is displayed
    search_page.load()
    assert search_page.get_logo() is not None

    # When the user searches for "panda"
    search_page.search_phrase(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.get_search_box_value()

    # And the search result links pertain to "panda"
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()

    # Then the search result title contains "panda"
    assert phrase in result_page.get_title()
