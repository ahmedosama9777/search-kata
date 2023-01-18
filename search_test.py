from unittest import TestCase

from search import Search


class TestSearch(TestCase):
    def test_search_text_less_than_two_chars_returns_no_results(self):
        search_engine = Search()
        self.assertEqual(search_engine.search("r"), [])

    def test_search_returns_city_starting_with_search_text(self):
        search_engine = Search()
        self.assertEqual(search_engine.search("Va"), ["Valencia", "Vancouver"])
