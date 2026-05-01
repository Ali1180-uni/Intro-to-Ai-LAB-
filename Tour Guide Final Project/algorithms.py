from data_store import fetch_all_countries, get_country

# ─── BFS ────────────────────────────────────────────
def bfs_neighbors(start_code, max_hops=2):
    """Find all countries reachable within N border hops"""
    all_data = fetch_all_countries()
    visited = set()
    queue = [(start_code, 0)]
    result = []

    while queue:
        code, hops = queue.pop(0)
        if code in visited or hops > max_hops:
            continue
        visited.add(code)
        country = all_data.get(code)
        if not country:
            continue
        result.append(country)
        for border in country.get("borders", []):
            if border not in visited:
                queue.append((border, hops + 1))

    return result

# ─── BFS PATH ───────────────────────────────────────
def bfs_path(start_code, end_code):
    """Shortest border path between 2 countries"""
    all_data = fetch_all_countries()
    queue = [[start_code]]
    visited = set()

    while queue:
        path = queue.pop(0)
        code = path[-1]
        if code == end_code:
            return [all_data[c] for c in path if c in all_data]
        if code in visited:
            continue
        visited.add(code)
        country = all_data.get(code)
        if not country:
            continue
        for border in country.get("borders", []):
            queue.append(path + [border])

    return []  # no path found

# ─── MINIMAX SCORING ────────────────────────────────
def score_country(country, current_region):
    """Score a country as next destination"""
    score = 0
    score += len(country.get("borders", [])) * 10      # connected = good
    if country.get("region") == current_region:
        score += 30                                      # same region = nearby
    pop = country.get("population", 0)
    if pop < 50_000_000:
        score += 20                                      # less crowded = better
    return score

def minimax_recommend(current_code, top_n=3):
    """Recommend top N next countries to visit"""
    all_data = fetch_all_countries()
    current = all_data.get(current_code)
    if not current:
        return []
    
    region = current.get("region", "")
    neighbors = bfs_neighbors(current_code, max_hops=1)
    
    scored = []
    for c in neighbors:
        if c["alpha3Code"] == current_code:
            continue
        s = score_country(c, region)
        scored.append((s, c))
    
    scored.sort(reverse=True)
    return [c for _, c in scored[:top_n]]


import math


def minimax_score(country, all_countries=None):
    """Compute score: -log(population) + (tourism_index / 10).

    `all_countries` kept for API consistency; not required here.
    """
    pop = country.get("population") or 1
    tourism = country.get("tourism_index") or country.get("tourism") or 0
    try:
        return -math.log(max(int(pop), 1)) + (float(tourism) / 10.0)
    except Exception:
        return 0.0


def smart_trip_recommend(start_country, num_countries, all_countries):
    """Return a route (list of country dicts) starting from `start_country`.

    - If `start_country` is a string, it's treated as an alpha3 code.
    - num_countries == 1: returns [start, best_neighbor] using `minimax_recommend`.
    - num_countries >= 2: builds a BFS-like chain: start -> best neighbor -> best neighbor ...
    Each returned country dict gets a `score` key (float) computed by `minimax_score`.
    """
    # normalize start code
    if isinstance(start_country, dict):
        start_code = start_country.get("alpha3Code")
    else:
        start_code = (start_country or "").upper()

    if not start_code or start_code not in all_countries:
        return []

    # single country case: start + best neighbor by minimax_score
    if num_countries <= 1:
        route = []
        start = all_countries.get(start_code)
        if start:
            start = dict(start)
            start["score"] = minimax_score(start, all_countries)
            route.append(start)

        neighbors = bfs_neighbors(start_code, max_hops=1)
        best = None
        best_score = float("-inf")
        for n in neighbors:
            if n.get("alpha3Code") == start_code:
                continue
            s = minimax_score(n, all_countries)
            if s > best_score:
                best_score = s
                best = n
        if best:
            best = dict(best)
            best["score"] = minimax_score(best, all_countries)
            route.append(best)
        return route

    # multi-country chain
    route = []
    visited = set()
    code = start_code
    for _ in range(num_countries):
        country = all_countries.get(code)
        if not country:
            break
        ccopy = dict(country)
        ccopy["score"] = minimax_score(ccopy, all_countries)
        route.append(ccopy)
        visited.add(code)

        # find immediate neighbors via existing bfs_neighbors (max_hops=1)
        neighbors = bfs_neighbors(code, max_hops=1)
        best_code = None
        best_score = float("-inf")
        for n in neighbors:
            ncode = n.get("alpha3Code")
            if not ncode or ncode in visited:
                continue
            s = minimax_score(n, all_countries)
            if s > best_score:
                best_score = s
                best_code = ncode

        if not best_code:
            break
        code = best_code

    return route