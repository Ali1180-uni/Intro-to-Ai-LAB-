import tkinter as tk
from tkinter import ttk, messagebox
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from map_view import build_route_figure, build_population_figure

# ── Flask base URL ──
BASE = "http://localhost:5000/api"

class TourGuideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tour Guide System")
        self.root.geometry("980x680")
        self.current_code = None
        self.current_country = None
        self.route = []
        self.map_canvas = None
        self.stats_canvas = None
        self.build_ui()

    def build_ui(self):
        # ── Search Bar ──
        top = tk.Frame(self.root, bg="#2c3e50", pady=10)
        top.pack(fill="x")

        tk.Label(top, text="Tour Guide System",
             font=("Arial", 18, "bold"),
             bg="#2c3e50", fg="white").pack()

        search_frame = tk.Frame(top, bg="#2c3e50")
        search_frame.pack()
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var,
             font=("Arial", 13), width=36).pack(side="left", padx=5)
        tk.Button(search_frame, text="Plan Trip",
              command=self.plan_trip,
              bg="#e74c3c", fg="white").pack(side="left")

        options_frame = tk.Frame(top, bg="#2c3e50")
        options_frame.pack(pady=6)
        tk.Label(options_frame, text="Total Countries",
             bg="#2c3e50", fg="white").pack(side="left", padx=6)
        self.count_var = tk.StringVar(value="3")
        tk.Entry(options_frame, textvariable=self.count_var,
             font=("Arial", 12), width=6).pack(side="left")

        # ── Info Panel ──
        self.info_frame = tk.Frame(self.root, bg="#ecf0f1", pady=10)
        self.info_frame.pack(fill="x", padx=20)
        self.info_label = tk.Label(self.info_frame,
                   text="Enter countries (comma-separated) to plan your route.",
                   font=("Arial", 12), bg="#ecf0f1")
        self.info_label.pack()

        # ── Recommendations ──
        rec_frame = tk.LabelFrame(self.root,
                  text="Route (best order by population)",
                  font=("Arial", 11, "bold"), padx=10, pady=10)
        rec_frame.pack(fill="x", padx=20, pady=5)
        self.rec_list = tk.Listbox(rec_frame, height=5, font=("Arial", 11))
        self.rec_list.pack(fill="x")

        # ── Buttons ──
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Show Route",
              command=self.refresh_route,
              bg="#27ae60", fg="white",
              font=("Arial", 11), width=15).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Refresh Stats",
              command=self.refresh_stats,
              bg="#d35400", fg="white",
              font=("Arial", 11), width=15).pack(side="left", padx=5)

        # ── Visuals ──
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        self.map_tab = tk.Frame(self.notebook, bg="#f4f7fb")
        self.stats_tab = tk.Frame(self.notebook, bg="#fbf7f2")
        self.notebook.add(self.map_tab, text="Map")
        self.notebook.add(self.stats_tab, text="Stats")

    def plan_trip(self):
        countries_input = self.search_var.get().strip()
        if not countries_input:
            messagebox.showwarning("Wait", "Enter at least one country")
            return

        try:
            count = int(self.count_var.get() or 3)
        except ValueError:
            count = 3

        res = requests.get(
            f"{BASE}/plan",
            params={"countries": countries_input, "count": count},
            timeout=20,
        )
        if res.status_code != 200:
            messagebox.showerror("Error", "Could not build route")
            return

        self.route = res.json()
        if not self.route:
            messagebox.showerror("Error", "Route is empty")
            return

        self.current_country = self.route[0]
        self.current_code = self.current_country.get("alpha3Code")

        self._render_route_list()
        self._render_summary()
        self.refresh_route()
        self.refresh_stats()

    def _render_route_list(self):
        self.rec_list.delete(0, tk.END)
        for i, r in enumerate(self.route, start=1):
            pop = r.get("population", 0)
            score = r.get("score", 0.0)
            self.rec_list.insert(tk.END,
                f"{i}. {r.get('name','')} | pop: {pop:,} | score: {score:.4f}")

    def _render_summary(self):
        total_pop = sum(c.get("population", 0) for c in self.route)
        start = self.route[0].get("name", "")
        end = self.route[-1].get("name", "")
        info = (
            f"Start: {start}   End: {end}   "
            f"Total Countries: {len(self.route)}   "
            f"Total Population: {total_pop:,}"
        )
        self.info_label.config(text=info)

    def refresh_route(self):
        if not self.route:
            messagebox.showwarning("Wait", "Plan a trip first")
            return
        fig = build_route_figure(self.route)
        self._set_canvas(self.map_tab, fig, "map")

    def refresh_stats(self):
        if not self.route:
            messagebox.showwarning("Wait", "Plan a trip first")
            return
        fig = build_population_figure(self.route)
        self._set_canvas(self.stats_tab, fig, "stats")

    def _set_canvas(self, parent, fig, which):
        if which == "map" and self.map_canvas:
            self.map_canvas.get_tk_widget().destroy()
        if which == "stats" and self.stats_canvas:
            self.stats_canvas.get_tk_widget().destroy()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        if which == "map":
            self.map_canvas = canvas
        else:
            self.stats_canvas = canvas

if __name__ == "__main__":
    root = tk.Tk()
    app = TourGuideApp(root)
    root.mainloop()