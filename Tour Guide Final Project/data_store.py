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

def _normalize_currencies(raw):
    if not isinstance(raw, dict):
        return []
    result = []
    for cur in raw.values():
        if not isinstance(cur, dict):
            continue
        result.append({
            "name": cur.get("name") or "",
            "symbol": cur.get("symbol") or "",
        })
    return result


def fetch_all_countries():
    if _cache:
        return _cache  # already fetched, reuse

    url = "https://restcountries.com/v3.1/all"
    fields = "name,cca3,capital,region,population,latlng,borders,currencies"
    res = requests.get(url, params={"fields": fields}, timeout=20)
    res.raise_for_status()
    countries = res.json()

    for c in countries:
        name = (c.get("name") or {}).get("common") or ""
        capital_list = c.get("capital") or []
        capital = capital_list[0] if capital_list else ""
        normalized = {
            "alpha3Code": c.get("cca3") or "",
            "name": name,
            "capital": capital,
            "region": c.get("region") or "",
            "population": c.get("population") or 0,
            "latlng": c.get("latlng") or [],
            "borders": c.get("borders") or [],
            "currencies": _normalize_currencies(c.get("currencies")),
        }
        if not normalized["alpha3Code"]:
            continue

        # attach famous locations for all countries (overrides + fallback)
        normalized["famous_locations"] = _FAMOUS_OVERRIDES.get(name, _default_locations(normalized))
        _cache[normalized["alpha3Code"]] = normalized  # key = "PAK", "IND" etc

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