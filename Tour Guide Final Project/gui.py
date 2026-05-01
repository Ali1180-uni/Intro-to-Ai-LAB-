import tkinter as tk
from tkinter import ttk, messagebox
import requests
from algorithms import bfs_neighbors, minimax_recommend, bfs_path
from map_view import generate_map
from selenium_runner import open_map
import turtle

# ── Flask base URL ──
BASE = "http://localhost:5000"

class TourGuideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Tour Guide")
        self.root.geometry("900x600")
        self.current_code = None
        self.build_ui()

    def build_ui(self):
        # ── Search Bar ──
        top = tk.Frame(self.root, bg="#2c3e50", pady=10)
        top.pack(fill="x")

        tk.Label(top, text="🌍 AI Tour Guide",
                 font=("Arial", 18, "bold"),
                 bg="#2c3e50", fg="white").pack()

        search_frame = tk.Frame(top, bg="#2c3e50")
        search_frame.pack()
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var,
                 font=("Arial", 13), width=30).pack(side="left", padx=5)
        tk.Button(search_frame, text="Search",
                  command=self.search_country,
                  bg="#e74c3c", fg="white").pack(side="left")

        # ── Info Panel ──
        self.info_frame = tk.Frame(self.root, bg="#ecf0f1", pady=10)
        self.info_frame.pack(fill="x", padx=20)
        self.info_label = tk.Label(self.info_frame,
                                   text="Search a country to start...",
                                   font=("Arial", 12), bg="#ecf0f1")
        self.info_label.pack()

        # ── Recommendations ──
        rec_frame = tk.LabelFrame(self.root,
                                  text="🤖 Minimax Recommendations",
                                  font=("Arial", 11, "bold"), padx=10, pady=10)
        rec_frame.pack(fill="x", padx=20, pady=5)
        self.rec_list = tk.Listbox(rec_frame, height=3, font=("Arial", 11))
        self.rec_list.pack(fill="x")

        # ── Buttons ──
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🗺️ Show Map",
                  command=self.show_map,
                  bg="#27ae60", fg="white",
                  font=("Arial", 11), width=15).pack(side="left", padx=5)

        tk.Button(btn_frame, text="🐢 Draw Path",
                  command=self.draw_turtle_path,
                  bg="#8e44ad", fg="white",
                  font=("Arial", 11), width=15).pack(side="left", padx=5)

    def search_country(self):
        name = self.search_var.get()
        res = requests.get(f"{BASE}/country/{name}")
        if res.status_code != 200:
            messagebox.showerror("Error", "Country not found")
            return

        c = res.json()
        self.current_code = c["alpha3Code"]
        self.current_country = c

        # show info
        info = (f"🏙 Capital: {c.get('capital','N/A')}   "
                f"🌍 Region: {c.get('region','N/A')}   "
                f"👥 Population: {c.get('population',0):,}   "
                f"💰 Currency: {c['currencies'][0]['name'] if c.get('currencies') else 'N/A'}")
        self.info_label.config(text=info)

        # get recommendations
        recs = minimax_recommend(self.current_code)
        self.rec_list.delete(0, tk.END)
        self.recommendations = recs
        for r in recs:
            self.rec_list.insert(tk.END,
                f"✈ {r['name']} | {r.get('capital','?')} | {r.get('region','?')}")

    def show_map(self):
        if not self.current_code:
            messagebox.showwarning("Wait", "Search country first")
            return
        recs = minimax_recommend(self.current_code)
        route = [self.current_country] + recs
        generate_map(route)
        open_map()

    def draw_turtle_path(self):
        if not self.current_code or not hasattr(self, 'recommendations'):
            return
        route = [self.current_country] + self.recommendations
        t = turtle.Turtle()
        t.speed(3)
        screen = turtle.Screen()
        screen.title("Travel Path")

        positions = []
        for c in route:
            latlng = c.get("latlng", [0, 0])
            # scale lat/lng to screen coords
            x = latlng[1] * 2   # lng → x
            y = latlng[0] * 2   # lat → y
            positions.append((x, y, c["name"]))

        t.penup()
        for i, (x, y, name) in enumerate(positions):
            t.goto(x, y)
            t.pendown()
            t.dot(10, "red")
            t.write(name, font=("Arial", 8))
        
        turtle.done()

if __name__ == "__main__":
    root = tk.Tk()
    app = TourGuideApp(root)
    root.mainloop()