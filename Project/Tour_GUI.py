import threading
import time
from typing import List, Tuple

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests


API_URL = "http://127.0.0.1:5000"

THEME = {
	"bg": "#141414",
	"sidebar": "#1f1f1f",
	"accent": "#E50914",
	"text": "#FFFFFF",
	"muted": "#B3B3B3",
	"card": "#1b1b1b",
	"glass": "#202020",
}


def parse_sections(text: str) -> List[Tuple[str, List[str]]]:
	sections: List[Tuple[str, List[str]]] = []
	current_title = ""
	current_items: List[str] = []

	for raw_line in text.splitlines():
		line = raw_line.strip()
		if not line:
			continue
		if line.endswith(":"):
			if current_title:
				sections.append((current_title, current_items))
			current_title = line[:-1]
			current_items = []
			continue
		if line.startswith("-") or line.startswith("*"):
			current_items.append(line.lstrip("-* ").strip())
		else:
			current_items.append(line)

	if current_title:
		sections.append((current_title, current_items))

	return sections


class ApiClient:
	def __init__(self, base_url: str) -> None:
		self.base_url = base_url
		self.session = requests.Session()

	def signup(self, username: str, password: str) -> dict:
		return self._post("/signup", {"username": username, "password": password})

	def login(self, username: str, password: str) -> dict:
		return self._post("/login", {"username": username, "password": password})

	def logout(self) -> dict:
		return self._post("/logout", {})

	def get_profile(self) -> dict:
		return self._get("/profile")

	def save_profile(self, payload: dict) -> dict:
		return self._put("/profile", payload)

	def recommend(self, query: str) -> dict:
		return self._post("/recommendations", {"query": query})

	def history(self) -> list:
		return self._get("/history")

	def search(self, query: str) -> list:
		return self._get("/search", params={"q": query})

	def itinerary(self, days: int, theme: str) -> dict:
		return self._post("/itinerary", {"days": days, "theme": theme})

	def save_favorite(self, title: str, details: str) -> dict:
		return self._post("/favorites", {"title": title, "details": details})

	def favorites(self) -> list:
		return self._get("/favorites")

	def _get(self, path: str, params: dict | None = None) -> dict:
		response = self.session.get(self.base_url + path, params=params, timeout=20)
		response.raise_for_status()
		return response.json()

	def _post(self, path: str, payload: dict) -> dict:
		response = self.session.post(self.base_url + path, json=payload, timeout=20)
		response.raise_for_status()
		return response.json()

	def _put(self, path: str, payload: dict) -> dict:
		response = self.session.put(self.base_url + path, json=payload, timeout=20)
		response.raise_for_status()
		return response.json()


class TourGuideApp(ctk.CTk):
	def __init__(self) -> None:
		super().__init__()
		ctk.set_appearance_mode("dark")
		ctk.set_default_color_theme("dark-blue")

		self.title("AI Tour Guide")
		self.geometry("1200x760")
		self.minsize(1050, 700)
		self.configure(fg_color=THEME["bg"])

		self.api = ApiClient(API_URL)
		self.loading = False
		self.loading_frames: List[tk.Label] = []
		self.last_response = ""

		self.login_frame = LoginFrame(self, self.api, self.on_login_success)
		self.dashboard = DashboardFrame(self, self.api, self.on_logout)
		self.show_login()

	def show_login(self) -> None:
		self.dashboard.pack_forget()
		self.login_frame.pack(fill="both", expand=True)

	def show_dashboard(self) -> None:
		self.login_frame.pack_forget()
		self.dashboard.pack(fill="both", expand=True)

	def on_login_success(self) -> None:
		self.dashboard.load_profile()
		self.show_dashboard()

	def on_logout(self) -> None:
		self.api.logout()
		self.show_login()


class LoginFrame(ctk.CTkFrame):
	def __init__(self, master: TourGuideApp, api: ApiClient, on_success) -> None:
		super().__init__(master, fg_color=THEME["bg"])
		self.api = api
		self.on_success = on_success

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(0, weight=1)

		brand_panel = ctk.CTkFrame(self, fg_color=THEME["sidebar"], corner_radius=20)
		brand_panel.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

		title = ctk.CTkLabel(
			brand_panel,
			text="AI Tour Guide",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 36, "bold"),
		)
		title.pack(pady=(80, 10))

		subtitle = ctk.CTkLabel(
			brand_panel,
			text="Smart travel planning\nNetflix-inspired premium UI",
			text_color=THEME["muted"],
			font=ctk.CTkFont("Segoe UI", 16),
		)
		subtitle.pack()

		form_panel = ctk.CTkFrame(self, fg_color=THEME["glass"], corner_radius=20)
		form_panel.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

		ctk.CTkLabel(
			form_panel,
			text="Welcome Back",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 28, "bold"),
		).pack(pady=(60, 10))

		self.username_entry = ctk.CTkEntry(
			form_panel,
			width=320,
			height=42,
			placeholder_text="Username",
			fg_color="#242424",
			text_color=THEME["text"],
		)
		self.username_entry.pack(pady=(10, 10))

		self.password_entry = ctk.CTkEntry(
			form_panel,
			width=320,
			height=42,
			placeholder_text="Password",
			show="*",
			fg_color="#242424",
			text_color=THEME["text"],
		)
		self.password_entry.pack(pady=(0, 20))

		self.login_btn = ctk.CTkButton(
			form_panel,
			text="Login",
			fg_color=THEME["accent"],
			hover_color="#f11f2b",
			width=320,
			height=44,
			command=self.handle_login,
		)
		self.login_btn.pack(pady=(0, 10))

		self.signup_btn = ctk.CTkButton(
			form_panel,
			text="Signup",
			fg_color="#303030",
			hover_color="#3c3c3c",
			width=320,
			height=44,
			command=self.handle_signup,
		)
		self.signup_btn.pack(pady=(0, 20))

		self.status_label = ctk.CTkLabel(
			form_panel,
			text="",
			text_color=THEME["muted"],
			font=ctk.CTkFont("Segoe UI", 12),
		)
		self.status_label.pack(pady=(10, 0))

	def handle_login(self) -> None:
		username = self.username_entry.get().strip()
		password = self.password_entry.get().strip()
		if not username or not password:
			messagebox.showwarning("Missing", "Enter username and password.")
			return

		try:
			self.api.login(username, password)
			self.status_label.configure(text="Login successful")
			self.on_success()
		except Exception as exc:
			messagebox.showerror("Login failed", str(exc))

	def handle_signup(self) -> None:
		username = self.username_entry.get().strip()
		password = self.password_entry.get().strip()
		if not username or not password:
			messagebox.showwarning("Missing", "Enter username and password.")
			return

		try:
			self.api.signup(username, password)
			messagebox.showinfo("Signup", "Account created. Now login.")
		except Exception as exc:
			messagebox.showerror("Signup failed", str(exc))


class DashboardFrame(ctk.CTkFrame):
	def __init__(self, master: TourGuideApp, api: ApiClient, on_logout) -> None:
		super().__init__(master, fg_color=THEME["bg"])
		self.api = api
		self.on_logout = on_logout

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

		self.sidebar = Sidebar(self, self.show_view, self.on_logout)
		self.sidebar.grid(row=0, column=0, sticky="nsew")

		self.content = ctk.CTkFrame(self, fg_color=THEME["bg"], corner_radius=0)
		self.content.grid(row=0, column=1, sticky="nsew")
		self.content.grid_rowconfigure(0, weight=1)
		self.content.grid_columnconfigure(0, weight=1)

		self.home_view = HomeView(self.content, self.show_view)
		self.chat_view = ChatView(self.content, self.api)
		self.profile_view = ProfileView(self.content, self.api)

		self.show_view("Home")

	def show_view(self, name: str) -> None:
		for child in self.content.winfo_children():
			child.grid_forget()
		if name == "Home":
			self.home_view.grid(row=0, column=0, sticky="nsew")
		elif name == "AI Tour Chatbot":
			self.chat_view.grid(row=0, column=0, sticky="nsew")
		elif name == "Profile":
			self.profile_view.grid(row=0, column=0, sticky="nsew")

	def load_profile(self) -> None:
		self.profile_view.load_profile()


class Sidebar(ctk.CTkFrame):
	def __init__(self, master, on_nav, on_logout) -> None:
		super().__init__(master, fg_color=THEME["sidebar"], corner_radius=0)
		self.on_nav = on_nav
		self.on_logout = on_logout

		self.grid_rowconfigure(6, weight=1)
		self.grid_columnconfigure(0, weight=1)

		ctk.CTkLabel(
			self,
			text="Tour Guide",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 22, "bold"),
		).grid(row=0, column=0, padx=20, pady=(30, 20), sticky="w")

		self._add_button("Home", 1)
		self._add_button("AI Tour Chatbot", 2)
		self._add_button("Profile", 3)

		logout_btn = ctk.CTkButton(
			self,
			text="Logout",
			fg_color="#2b2b2b",
			hover_color="#3a3a3a",
			text_color=THEME["text"],
			command=self.on_logout,
		)
		logout_btn.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

	def _add_button(self, label: str, row: int) -> None:
		btn = ctk.CTkButton(
			self,
			text=label,
			fg_color="#2b2b2b",
			hover_color="#3a3a3a",
			text_color=THEME["text"],
			command=lambda: self.on_nav(label),
		)
		btn.grid(row=row, column=0, padx=20, pady=8, sticky="ew")


class HomeView(ctk.CTkFrame):
	def __init__(self, master, on_nav) -> None:
		super().__init__(master, fg_color=THEME["bg"])
		self.on_nav = on_nav

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=1)
		self.grid_columnconfigure(0, weight=1)

		ctk.CTkLabel(
			self,
			text="AI Tour Guide System",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 40, "bold"),
		).grid(row=1, column=0, sticky="s")

		button_row = ctk.CTkFrame(self, fg_color=THEME["bg"], corner_radius=0)
		button_row.grid(row=2, column=0, pady=(20, 80))

		ctk.CTkButton(
			button_row,
			text="Set Preference",
			fg_color=THEME["accent"],
			hover_color="#f11f2b",
			width=220,
			height=46,
			command=lambda: self.on_nav("Profile"),
		).grid(row=0, column=0, padx=10)

		ctk.CTkButton(
			button_row,
			text="Chat With Tour Agent",
			fg_color="#2b2b2b",
			hover_color="#3a3a3a",
			width=260,
			height=46,
			command=lambda: self.on_nav("AI Tour Chatbot"),
		).grid(row=0, column=1, padx=10)


class ChatView(ctk.CTkFrame):
	def __init__(self, master, api: ApiClient) -> None:
		super().__init__(master, fg_color=THEME["bg"])
		self.api = api
		self.loading = False
		self.last_response = ""

		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)

		header = ctk.CTkFrame(self, fg_color=THEME["bg"], corner_radius=0)
		header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(20, 10))
		header.grid_columnconfigure(0, weight=1)

		ctk.CTkLabel(
			header,
			text="AI Tour Chatbot",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 22, "bold"),
		).grid(row=0, column=0, sticky="w")



		self.chat_area = ctk.CTkScrollableFrame(self, fg_color=THEME["bg"], corner_radius=0)
		self.chat_area.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
		self._bind_smooth_scroll(self.chat_area)

		input_bar = ctk.CTkFrame(self, fg_color=THEME["bg"], corner_radius=0)
		input_bar.grid(row=2, column=0, columnspan=1, sticky="ew", padx=20, pady=(0, 20))
		input_bar.grid_columnconfigure(0, weight=1)

		self.message_entry = ctk.CTkEntry(
			input_bar,
			placeholder_text="Ask about destinations, budgets, or travel tips...",
			height=44,
			fg_color="#1f1f1f",
			text_color=THEME["text"],
		)
		self.message_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

		self.send_btn = ctk.CTkButton(
			input_bar,
			text="Send",
			fg_color=THEME["accent"],
			hover_color="#f11f2b",
			width=120,
			command=self.send_message,
		)
		self.send_btn.grid(row=0, column=1)

		self.favorite_btn = ctk.CTkButton(
			input_bar,
			text="Save Favorite",
			fg_color="#2b2b2b",
			hover_color="#3a3a3a",
			width=140,
			command=self.save_favorite,
		)
		self.favorite_btn.grid(row=0, column=2, padx=(10, 0))

		self.loading_label = ctk.CTkLabel(
			input_bar,
			text="",
			text_color=THEME["muted"],
			font=ctk.CTkFont("Segoe UI", 12),
		)
		self.loading_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=(6, 0))

		self._seed_welcome()

	def _seed_welcome(self) -> None:
		self.add_message("assistant", "Hi! Share your destination or travel style to start.")

	def add_message(self, role: str, text: str) -> None:
		bubble = ctk.CTkFrame(
			self.chat_area,
			fg_color=THEME["card"] if role == "assistant" else "#2b2b2b",
			corner_radius=18,
		)
		bubble.pack(fill="x", padx=6, pady=6)

		ctk.CTkLabel(
			bubble,
			text=text,
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 13),
			justify="left",
			wraplength=420,
		).pack(padx=16, pady=12, anchor="w")

	def show_loading(self, active: bool) -> None:
		self.loading = active
		if active:
			self.loading_label.configure(text="Thinking")
			self._animate_loading(0)
		else:
			self.loading_label.configure(text="")

	def _animate_loading(self, tick: int) -> None:
		if not self.loading:
			return
		dots = "." * ((tick % 3) + 1)
		self.loading_label.configure(text=f"Thinking{dots}")
		self.after(400, lambda: self._animate_loading(tick + 1))

	def send_message(self) -> None:
		query = self.message_entry.get().strip()
		if not query:
			return
		self.message_entry.delete(0, tk.END)
		self.add_message("user", query)
		self.show_loading(True)

		thread = threading.Thread(target=self._fetch_ai, args=(query,), daemon=True)
		thread.start()

	def _fetch_ai(self, query: str) -> None:
		try:
			response = self.api.recommend(query)
			content = response.get("content", "")
			self.last_response = content
			self.after(0, lambda: self._render_ai(content))
		except Exception as exc:
			self.after(0, lambda: messagebox.showerror("AI Error", str(exc)))
		finally:
			self.after(0, lambda: self.show_loading(False))

	def _render_ai(self, content: str) -> None:
		self.add_message("assistant", "")
		last_bubble = self.chat_area.winfo_children()[-1]
		self._type_text(last_bubble, content)
		self._render_cards(content)

	def _type_text(self, bubble: ctk.CTkFrame, content: str) -> None:
		label = ctk.CTkLabel(
			bubble,
			text="",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 13),
			justify="left",
			wraplength=420,
		)
		label.pack(padx=16, pady=12, anchor="w")

		def step(index: int) -> None:
			if index > len(content):
				return
			label.configure(text=content[:index])
			self.after(6, lambda: step(index + 1))

		step(1)

	def _render_cards(self, content: str) -> None:
		for title, items in parse_sections(content):
			card = ctk.CTkFrame(self.chat_area, fg_color=THEME["card"], corner_radius=18)
			card.pack(fill="x", padx=6, pady=8)

			ctk.CTkLabel(
				card,
				text=title,
				text_color=THEME["text"],
				font=ctk.CTkFont("Segoe UI", 14, "bold"),
			).pack(anchor="w", padx=16, pady=(12, 4))

			for item in items[:6]:
				ctk.CTkLabel(
					card,
					text=f"- {item}",
					text_color=THEME["muted"],
					font=ctk.CTkFont("Segoe UI", 12),
					justify="left",
				).pack(anchor="w", padx=16, pady=2)

			ctk.CTkLabel(card, text="", height=2).pack(pady=(0, 8))

	def _bind_smooth_scroll(self, frame: ctk.CTkScrollableFrame) -> None:
		canvas = frame._parent_canvas

		def on_mousewheel(event: tk.Event) -> None:
			canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

		frame.bind_all("<MouseWheel>", on_mousewheel)

	def save_favorite(self) -> None:
		if not self.last_response:
			messagebox.showinfo("Favorites", "Generate a recommendation first.")
			return
		title = time.strftime("Tour %b %d")
		try:
			self.api.save_favorite(title, self.last_response)
			messagebox.showinfo("Favorites", "Saved to favorites.")
		except Exception as exc:
			messagebox.showerror("Favorites", str(exc))




class ProfileView(ctk.CTkFrame):
	def __init__(self, master, api: ApiClient) -> None:
		super().__init__(master, fg_color=THEME["bg"])
		self.api = api

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)

		header = ctk.CTkFrame(self, fg_color=THEME["bg"], corner_radius=0)
		header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
		ctk.CTkLabel(
			header,
			text="Profile",
			text_color=THEME["text"],
			font=ctk.CTkFont("Segoe UI", 22, "bold"),
		).pack(anchor="w")

		form = ctk.CTkFrame(self, fg_color=THEME["glass"], corner_radius=20)
		form.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
		form.grid_columnconfigure((0, 1), weight=1)

		self.name_entry = self._add_entry(form, "Name", 0, 0)
		self.age_entry = self._add_entry(form, "Age", 0, 1)
		self.country_entry = self._add_entry(form, "Country", 1, 0)
		self.people_entry = self._add_entry(form, "Number of People", 1, 1)

		self.preference_menu = self._add_option(
			form, "Travel Preference", 2, 0,
			["Beach", "Hills", "Historical", "Adventure", "Religious"],
		)
		self.weather_menu = self._add_option(
			form, "Weather Preference", 2, 1,
			["Sunny", "Cold", "Mild", "Snowy", "Rainy"],
		)
		self.food_menu = self._add_option(
			form, "Food Preference", 3, 0,
			["Seafood", "Local", "Vegetarian", "Street Food", "Any"],
		)

		save_btn = ctk.CTkButton(
			form,
			text="Save Profile",
			fg_color=THEME["accent"],
			hover_color="#f11f2b",
			height=44,
			command=self.save_profile,
		)
		save_btn.grid(row=4, column=0, padx=24, pady=(20, 30), sticky="w")

	def _add_entry(self, parent, label: str, row: int, col: int) -> ctk.CTkEntry:
		ctk.CTkLabel(
			parent,
			text=label,
			text_color=THEME["muted"],
			font=ctk.CTkFont("Segoe UI", 12),
		).grid(row=row * 2, column=col, sticky="w", padx=24, pady=(20, 4))

		entry = ctk.CTkEntry(
			parent,
			height=40,
			fg_color="#242424",
			text_color=THEME["text"],
		)
		entry.grid(row=row * 2 + 1, column=col, sticky="ew", padx=24)
		return entry

	def _add_option(self, parent, label: str, row: int, col: int, values: List[str]) -> ctk.CTkOptionMenu:
		ctk.CTkLabel(
			parent,
			text=label,
			text_color=THEME["muted"],
			font=ctk.CTkFont("Segoe UI", 12),
		).grid(row=row * 2, column=col, sticky="w", padx=24, pady=(20, 4))

		menu = ctk.CTkOptionMenu(
			parent,
			values=values,
			fg_color="#242424",
			button_color=THEME["accent"],
			button_hover_color="#f11f2b",
			dropdown_hover_color="#2f2f2f",
			text_color=THEME["text"],
		)
		menu.grid(row=row * 2 + 1, column=col, sticky="ew", padx=24)
		return menu

	def load_profile(self) -> None:
		try:
			data = self.api.get_profile()
		except Exception as exc:
			messagebox.showerror("Profile", str(exc))
			return
		self.name_entry.delete(0, tk.END)
		self.name_entry.insert(0, data.get("name", ""))
		self.age_entry.delete(0, tk.END)
		self.age_entry.insert(0, data.get("age", ""))
		self.country_entry.delete(0, tk.END)
		self.country_entry.insert(0, data.get("country", ""))
		self.people_entry.delete(0, tk.END)
		self.people_entry.insert(0, data.get("people", ""))
		if data.get("preference"):
			self.preference_menu.set(data.get("preference"))
		if data.get("weather"):
			self.weather_menu.set(data.get("weather"))
		if data.get("food"):
			self.food_menu.set(data.get("food"))

	def save_profile(self) -> None:
		payload = {
			"name": self.name_entry.get().strip(),
			"age": self.age_entry.get().strip(),
			"country": self.country_entry.get().strip(),
			"people": self.people_entry.get().strip(),
			"preference": self.preference_menu.get(),
			"weather": self.weather_menu.get(),
			"food": self.food_menu.get(),
		}
		if not payload["name"]:
			messagebox.showwarning("Profile", "Name is required.")
			return
		try:
			self.api.save_profile(payload)
			messagebox.showinfo("Profile", "Profile saved.")
		except Exception as exc:
			messagebox.showerror("Profile", str(exc))


if __name__ == "__main__":
	app = TourGuideApp()
	app.mainloop()
