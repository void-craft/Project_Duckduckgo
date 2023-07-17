"""
This test covers expanding the search results,
by clicking the more results button.
"""

from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase', ['circle', 'rectangle', 'triangle'])
def test_expand_more_results(browser, phrase):
    result_page = ResultPage(browser)

    # Given the DuckDuckGo result page is displayed
    result_page.load_result_page(phrase)

    # Assert if title as search phrase
    assert phrase in result_page.get_title()

    # Assert if search result links have search phrase
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()

    # Get search results count
    original_count = result_page.find_result_count()

    # Assert if search box on result page has the search phrase
    assert phrase == result_page.get_search_box_value()

    # When the user clicks the More Results button
    result_page.click_more_results_link()

    # Then the user should see more search results
    assert original_count < result_page.find_result_count()



