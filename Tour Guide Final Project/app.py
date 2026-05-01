from flask import Flask, render_template, request
from data_store import fetch_all_countries, search_by_name
from algorithms import smart_trip_recommend, minimax_score
from map_view import generate_trip_map_html

app = Flask(__name__)


# Load all countries at startup and keep in memory
ALL_COUNTRIES = fetch_all_countries()


# app delegates scoring and recommendation to algorithms.smart_trip_recommend


@app.route("/")
def index():
    countries = sorted(ALL_COUNTRIES.values(), key=lambda c: c.get("name", ""))
    return render_template("index.html", countries=countries)


@app.route("/plan", methods=["POST"])
def plan():
    start = request.form.get("start")
    names_input = request.form.get("names")
    try:
        count = int(request.form.get("count") or 1)
    except ValueError:
        count = 1

    all_data = ALL_COUNTRIES
    def resolve_code(value):
        if not value:
            return None
        v = value.strip()
        if len(v) == 3 and v.upper() in all_data:
            return v.upper()
        res = search_by_name(v)
        if res:
            return res.get("alpha3Code")
        return None

    route = []
    selected_codes = []

    if names_input:
        parts = [p.strip() for p in names_input.split(",") if p.strip()]
        for p in parts:
            code = resolve_code(p)
            if code:
                selected_codes.append(code)
    else:
        code = resolve_code(start)
        if code:
            selected_codes.append(code)

    if not selected_codes:
        countries = sorted(all_data.values(), key=lambda c: c.get("name", ""))
        return render_template("index.html", countries=countries, error="Start country not found")

    # add user-provided countries first
    for code in selected_codes:
        c = all_data.get(code)
        if not c:
            continue
        ccopy = dict(c)
        ccopy["score"] = minimax_score(ccopy, all_data)
        route.append(ccopy)

    # auto-complete remaining route based on minimax scoring
    remaining = max(count - len(route), 0)
    if remaining > 0:
        last_code = route[-1].get("alpha3Code")
        extension = smart_trip_recommend(last_code, remaining, all_data)
        if extension:
            # extension includes the start country; skip it
            route.extend(extension[1:])

    # generate folium map html via map_view helper
    map_html = generate_trip_map_html(route)
    return render_template("results.html", route=route, map_html=map_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)