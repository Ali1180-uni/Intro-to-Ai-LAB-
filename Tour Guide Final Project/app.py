from flask import Flask, jsonify, request
from data_store import fetch_all_countries, search_by_name
from algorithms import minimax_recommend, minimax_score, plan_trip

app = Flask(__name__)


# Load all countries at startup and keep in memory
ALL_COUNTRIES = fetch_all_countries()


# app delegates scoring and recommendation to algorithms.smart_trip_recommend


def _resolve_code(value):
    if not value:
        return None
    v = value.strip()
    if len(v) == 3 and v.upper() in ALL_COUNTRIES:
        return v.upper()
    res = search_by_name(v)
    if res:
        return res.get("alpha3Code")
    return None


@app.route("/api/countries")
def api_countries():
    countries = sorted(ALL_COUNTRIES.values(), key=lambda c: c.get("name", ""))
    return jsonify([
        {"name": c.get("name"), "alpha3Code": c.get("alpha3Code")}
        for c in countries
    ])


@app.route("/api/country/<query>")
def api_country(query):
    code = _resolve_code(query)
    if not code:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(ALL_COUNTRIES.get(code))


@app.route("/api/recommend/<code>")
def api_recommend(code):
    code = (code or "").upper()
    if code not in ALL_COUNTRIES:
        return jsonify({"error": "Country not found"}), 404
    recs = minimax_recommend(code, all_data=ALL_COUNTRIES)
    return jsonify(recs)


@app.route("/api/plan")
def api_plan():
    countries_input = request.args.get("countries") or ""
    try:
        count = int(request.args.get("count") or 3)
    except ValueError:
        count = 3

    raw = [p.strip() for p in countries_input.split(",") if p.strip()]
    resolved = []
    for p in raw:
        code = _resolve_code(p)
        if code:
            resolved.append(code)

    if not resolved:
        return jsonify({"error": "No valid countries provided"}), 404

    route = plan_trip(resolved, count, ALL_COUNTRIES)
    for c in route:
        if "score" not in c:
            c["score"] = minimax_score(c)
    return jsonify(route)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)