class Search:
    CITIES = [
        "Paris",
        "Budapest",
        "Skopje",
        "Rotterdam",
        "Valencia",
        "Vancouver",
        "Amsterdam",
        "Vienna",
        "Sydney",
        "New York City",
        "London",
        "Bangkok",
        "Hong Kong",
        "Dubai",
        "Rome",
        "Istanbul",
    ]

    def search(self, search_text: str) -> list:
        if len(search_text) < 2:
            return []

        search_results: list[str] = []

        for city in self.CITIES:
            if city.startswith(search_text):
                search_results.append(city)

        return search_results
