from unittest import TestCase

from search import Search


class TestSearch(TestCase):
    def setUp(self):
        self.search_engine = Search()
    def test_search_text_less_than_two_chars_returns_no_results(self):
        self.assertEqual(self.search_engine.search("r"), [])

    def test_search_returns_city_starting_with_search_text(self):
        self.assertEqual(self.search_engine.search("Va"), ["Valencia", "Vancouver"])
    
    def test_search_is_case_sensitive(self):
        self.assertEqual(self.search_engine.search("va"), [])
    
    def test_search_returns_city_containing_search_text(self):
        self.assertEqual(self.search_engine.search("ape"), ["Budapest"])

    def test_search_returns_all_citiies_if_text_is_asterisk(self):
        self.assertEqual(self.search_engine.search("*"), self.search_engine.CITIES)