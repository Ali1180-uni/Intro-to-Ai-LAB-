from matplotlib.figure import Figure


def _route_points(trip_countries):
    points = []
    for c in trip_countries:
        latlng = c.get("latlng") or []
        if len(latlng) < 2:
            continue
        points.append((latlng[1], latlng[0], c.get("name", "")))  # lon, lat, name
    return points


def build_route_figure(trip_countries):
    """Build a matplotlib Figure showing the route on a simple world grid."""
    fig = Figure(figsize=(7.2, 4.2), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor("#f4f7fb")
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle="--", alpha=0.3)

    points = _route_points(trip_countries)
    if points:
        lons = [p[0] for p in points]
        lats = [p[1] for p in points]
        ax.plot(lons, lats, color="#1f77b4", linewidth=2, alpha=0.85)
        ax.scatter(lons, lats, color="#e74c3c", s=45, zorder=3)
        for i, (_, _, name) in enumerate(points):
            ax.annotate(name, (lons[i], lats[i]), fontsize=8, xytext=(3, 3), textcoords="offset points")

    ax.set_title("Trip Route")
    return fig


def build_population_figure(trip_countries):
    """Build a matplotlib Figure showing population bars for the route."""
    fig = Figure(figsize=(7.2, 3.8), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor("#fbf7f2")

    ordered = sorted(
        trip_countries,
        key=lambda c: c.get("score", 0.0),
        reverse=True,
    )
    names = [c.get("name", "") for c in ordered]
    pops = [c.get("population", 0) for c in ordered]
    ax.bar(names, pops, color="#2ca02c")
    ax.set_title("Best Countries by Population")
    ax.set_ylabel("Population")
    ax.tick_params(axis="x", labelrotation=25)
    fig.tight_layout()
    return fig