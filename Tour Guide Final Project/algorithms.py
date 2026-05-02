from collections import deque
import math
from data_store import fetch_all_countries

# ─── BFS ────────────────────────────────────────────
def bfs_neighbors(start_code, max_hops=2, all_data=None):
    """Find all countries reachable within N border hops."""
    all_data = all_data or fetch_all_countries()
    visited = set()
    queue = deque([(start_code, 0)])
    result = []

    while queue:
        code, hops = queue.popleft()
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
def bfs_path(start_code, end_code, all_data=None):
    """Shortest border path between 2 countries (list of codes)."""
    all_data = all_data or fetch_all_countries()
    queue = deque([[start_code]])
    visited = set()

    while queue:
        path = queue.popleft()
        code = path[-1]
        if code == end_code:
            return [c for c in path if c in all_data]
        if code in visited:
            continue
        visited.add(code)
        country = all_data.get(code)
        if not country:
            continue
        for border in country.get("borders", []):
            queue.append(path + [border])

    return []

# ─── MINIMAX SCORING ────────────────────────────────
def population_score(country):
    """Higher score means less crowded (population-based)."""
    pop = country.get("population") or 1
    safe_pop = max(int(pop), 1)
    return 1.0 / math.log(safe_pop + 1)

def minimax_recommend(current_code, top_n=3, all_data=None):
    """Recommend top N next countries by population score."""
    all_data = all_data or fetch_all_countries()
    current = all_data.get(current_code)
    if not current:
        return []

    neighbors = bfs_neighbors(current_code, max_hops=1, all_data=all_data)
    scored = []
    for c in neighbors:
        if c.get("alpha3Code") == current_code:
            continue
        scored.append((population_score(c), c))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [c for _, c in scored[:top_n]]


def minimax_score(country):
    """Expose population scoring for UI and API output."""
    return population_score(country)


def _normalize_codes(values, all_countries):
    codes = []
    for v in values:
        code = (v or "").strip().upper()
        if code and code in all_countries and code not in codes:
            codes.append(code)
    return codes


def plan_trip(selected_codes, total_count, all_countries):
    """Plan a trip using BFS paths and population-based minimax ranking."""
    codes = _normalize_codes(selected_codes, all_countries)
    if not codes:
        return []

    route_codes = [codes[0]]
    for nxt in codes[1:]:
        segment = bfs_path(route_codes[-1], nxt, all_data=all_countries)
        if segment:
            for code in segment[1:]:
                if code not in route_codes:
                    route_codes.append(code)
        elif nxt not in route_codes:
            route_codes.append(nxt)

    while len(route_codes) < max(int(total_count), 1):
        last = route_codes[-1]
        neighbors = bfs_neighbors(last, max_hops=1, all_data=all_countries)
        best = None
        best_score = float("-inf")
        for n in neighbors:
            code = n.get("alpha3Code")
            if not code or code in route_codes:
                continue
            score = population_score(n)
            if score > best_score:
                best_score = score
                best = code
        if not best:
            break
        route_codes.append(best)

    route = []
    for code in route_codes:
        country = all_countries.get(code)
        if not country:
            continue
        item = dict(country)
        item["score"] = population_score(item)
        route.append(item)

    return route