"""
This test covers searching for new phrase from the result page.
"""

from pages.result_page import ResultPage
import pytest


@pytest.mark.parametrize('phrase, new_phrase', [('circle', 'gold'), ('rectangle', 'lead'), ('triangle', 'tin')])
def test_search_from_result_page(browser, phrase, new_phrase):
    # Arrange: Create the ResultPage object
    result_page = ResultPage(browser)

    # Act: Perform the search with the original phrase
    result_page.load_result_page(phrase)

    # Assert: Check if the original phrase is present in the titles
    for title in result_page.get_result_link_titles():
        assert phrase.lower() in title.lower()

    # Act: Search for the new phrase from the page
    result_page.search_phrase(new_phrase)

    # Assert: Check if the new search phrase is present in the titles
    for title in result_page.get_result_link_titles():
        assert new_phrase.lower() in title.lower()

    # Assert: Check if search box has the new search phrase
    value = result_page.get_search_box_value()
    assert new_phrase in value
