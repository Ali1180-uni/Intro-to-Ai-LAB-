import folium
from folium.plugins import MiniMap


def generate_trip_map_html(trip_countries):
    """Return an embeddable HTML snippet for a trip (list of country dicts).

    - Start marker colored red
    - Other markers colored blue
    - Path polyline colored green
    - MiniMap control enabled
    """
    # Use an English-friendly tile set
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")
    coords = []

    for i, c in enumerate(trip_countries):
        latlng = c.get("latlng") or []
        if len(latlng) < 2:
            continue
        color = "red" if i == 0 else "blue"
        folium.CircleMarker(
            location=latlng,
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"{c.get('name')} | {c.get('capital','')}",
        ).add_to(m)
        coords.append(latlng)

    if len(coords) > 1:
        folium.PolyLine(coords, color="green", weight=3).add_to(m)

    MiniMap(toggle_display=True, tiles="CartoDB positron").add_to(m)

    # Return map HTML snippet (folium's _repr_html_ is a full <div> with inline scripts)
    return m._repr_html_()