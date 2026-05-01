import requests

_cache = {}  # store in memory, no DB


_FAMOUS_OVERRIDES = {
    "Pakistan": ["Badshahi Mosque", "Lahore Fort", "Faisal Mosque"],
    "Turkey": ["Hagia Sophia", "Cappadocia", "Blue Mosque"],
    "Greece": ["Acropolis", "Santorini", "Delphi"],
    "France": ["Eiffel Tower", "Louvre Museum", "Mont Saint-Michel"],
    "Italy": ["Colosseum", "Venice Grand Canal", "Leaning Tower of Pisa"],
    "United States of America": ["Grand Canyon", "Statue of Liberty", "Yellowstone"],
    "United Kingdom": ["Tower of London", "Stonehenge", "Edinburgh Castle"],
    "Spain": ["Sagrada Familia", "Alhambra", "Park Guell"],
    "Japan": ["Mount Fuji", "Fushimi Inari", "Tokyo Skytree"],
    "China": ["Great Wall", "Forbidden City", "Terracotta Army"],
    "India": ["Taj Mahal", "Amber Fort", "Varanasi Ghats"],
    "Egypt": ["Pyramids of Giza", "Valley of the Kings", "Karnak Temple"],
    "Saudi Arabia": ["Al-Ula", "Masjid al-Haram", "Riyadh Boulevard"],
}


def _default_locations(country):
    name = country.get("name", "")
    capital = country.get("capital") or name
    # Safe fallback list for every country
    return [
        f"{capital} Old City",
        f"{name} National Museum",
        f"{name} Central Park",
    ]

def fetch_all_countries():
    if _cache:
        return _cache  # already fetched, reuse
    
    res = requests.get("https://www.apicountries.com/countries")
    countries = res.json()
    
    for c in countries:
        # attach famous locations for all countries (overrides + fallback)
        if "famous_locations" not in c:
            c["famous_locations"] = _FAMOUS_OVERRIDES.get(c.get("name"), _default_locations(c))
        _cache[c["alpha3Code"]] = c  # key = "PAK", "IND" etc
    
    return _cache

def get_country(code):
    data = fetch_all_countries()
    return data.get(code)

def search_by_name(name):
    data = fetch_all_countries()
    for c in data.values():
        if name.lower() in c["name"].lower():
            return c
    return None