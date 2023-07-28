"""
1. This test covers verifying the auto complete suggestion.
2. Second test covers clicking the first auto suggestion link.
"""

from pages.search_page import SearchPage
from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase', ['where', 'why', 'what'])
def test_auto_complete(browser, phrase):
    search_page = SearchPage(browser)

    search_page.load()
    assert search_page.get_logo() is not None
    assert browser.title == "DuckDuckGo — Privacy, simplified."
    search_page.enter_search_item(phrase)
    suggestion_values = search_page.get_suggestion_values()
    assert phrase in suggestion_values


@pytest.mark.parametrize('phrase', ['where', 'why', 'what'])
def test_click_auto_suggestion_link(browser, phrase):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)

    search_page.load()
    assert search_page.get_logo() is not None
    assert browser.title == "DuckDuckGo — Privacy, simplified."
    search_page.enter_search_item(phrase)
    suggestion_values = search_page.get_suggestion_values()
    assert phrase in suggestion_values
    search_page.click_suggestion_link()
    assert phrase in result_page.get_title()
    assert phrase in result_page.get_search_box_value()
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()
