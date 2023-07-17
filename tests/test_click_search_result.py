"""
This test covers clicking the search result link.
"""

from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase', ['circle', 'rectangle', 'triangle'])
def test_click_search_result(browser, phrase):
    result_page = ResultPage(browser)

    # Given the DuckDuckGo result page is displayed
    result_page.load_result_page(phrase)

    # Assert if title as search phrase
    assert phrase in result_page.get_title()

    # Assert if search result links have search phrase
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()

    # Assert if search box on result page has the search phrase
    assert phrase == result_page.get_search_box_value()

    # Copy the first result link
    expected_url = result_page.get_first_result_link()

    # When the user clicks the search result link
    result_page.click_first_result_link()

    # Then the user should go to the relevant link
    assert browser.current_url == expected_url

