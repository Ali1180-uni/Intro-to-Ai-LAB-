import json
import os
import threading
import time
import uuid
import hashlib
from typing import Any, Dict, List

from flask import Flask, jsonify, request, session
from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROFILES_FILE = os.path.join(DATA_DIR, "profiles.json")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")
FAVORITES_FILE = os.path.join(DATA_DIR, "favorites.json")

FILE_LOCK = threading.Lock()

load_dotenv(os.path.join(BASE_DIR, ".env"))


def ensure_storage() -> None:
	os.makedirs(DATA_DIR, exist_ok=True)
	defaults = {
		USERS_FILE: {"users": {}},
		PROFILES_FILE: {"profiles": {}},
		HISTORY_FILE: {"history": {}},
		FAVORITES_FILE: {"favorites": {}},
	}

	for path, payload in defaults.items():
		if not os.path.exists(path):
			with open(path, "w", encoding="utf-8") as file:
				json.dump(payload, file, indent=2)


def read_json(path: str) -> Dict[str, Any]:
	with FILE_LOCK:
		with open(path, "r", encoding="utf-8") as file:
			return json.load(file)


def write_json(path: str, data: Dict[str, Any]) -> None:
	with FILE_LOCK:
		with open(path, "w", encoding="utf-8") as file:
			json.dump(data, file, indent=2)


def hash_password(password: str) -> str:
	return hashlib.sha256(password.encode("utf-8")).hexdigest()


def get_logged_in_user() -> str:
	return session.get("username", "")


def require_login() -> str:
	username = get_logged_in_user()
	if not username:
		raise PermissionError("Not authenticated")
	return username


def build_rules(preference: str) -> List[str]:
	pref_map = {
		"Beach": ["Maldives", "Bali", "Phuket"],
		"Hills": ["Hunza", "Swiss Alps", "Murree"],
		"Historical": ["Rome", "Cairo", "Istanbul"],
		"Adventure": ["Queenstown", "Skardu", "Patagonia"],
		"Religious": ["Makkah", "Madina", "Lahore"],
	}
	return pref_map.get(preference, ["Istanbul", "Dubai", "Baku"])


def build_prompt(profile: Dict[str, Any], extra_context: str) -> str:
	destinations = ", ".join(build_rules(profile.get("preference", "")))
	return (
		"You are an AI tour guide. Keep answers short and clean with headings and bullet points. "
		"Use these headings exactly: Tourist Attractions, Cheap Hotels, Premium Hotels, Estimated Cost, "
		"Food Recommendations, Packing Suggestions, Usual Weather, Currency. "
		"Avoid long paragraphs. Give 3-6 bullets per section. "
		"If the user mentions a city or country, respond specifically to that location. "
		"Never limit to a fixed list of destinations; rule-based destinations are only optional examples. "
		"Currency section must clearly state the local currency name and symbol. "
		"User Profile: "
		f"Name={profile.get('name')}, Age={profile.get('age')}, Country={profile.get('country')}, "
		f"People={profile.get('people')}, Preference={profile.get('preference')}, "
		f"Weather={profile.get('weather')}, Food={profile.get('food')}. "
		f"Rule-based destinations (examples only): {destinations}. "
		f"Extra context: {extra_context}"
	)


def get_local_response(message: str) -> str | None:
	text = message.strip().lower()
	if not text:
		return "Hi! Share a destination or travel style, and I will help."

	greetings = ("hi", "hello", "hey", "assalam", "salam")
	if text.startswith(greetings) or text in greetings:
		return "Hello! Tell me a city or country and your travel style."

	if "how are you" in text:
		return "I am great, thanks for asking. Ready to plan your trip."

	if "can you help" in text or "help me" in text:
		return "Yes. Tell me your destination, budget, and preference."

	if "what can you do" in text or "what do you do" in text:
		return "I suggest tours, hotels, costs, food, and packing tips."

	return None


def call_groq(prompt: str) -> str:
	api_key = os.getenv("GROQ_API_KEY", "").strip()
	if not api_key:
		return (
			"Tourist Attractions:\n"
			"- Maldives beaches\n- Bali temples\n- Phuket islands\n\n"
			"Cheap Hotels:\n"
			"- Coral Budget Inn\n- Coastline Guesthouse\n\n"
			"Premium Hotels:\n"
			"- Ocean Luxe Resort\n- Sunset Palace\n\n"
			"Estimated Cost:\n"
			"- 5 days: $900-$1400\n\n"
			"Food Recommendations:\n"
			"- Seafood platters\n- Tropical fruit bowls\n\n"
			"Packing Suggestions:\n"
			"- Sunscreen\n- Light jackets\n\n"
			"Usual Weather:\n"
			"- Warm, breezy evenings\n\n"
			"Currency:\n"
			"- Local Currency: USD, Symbol: $\n"
		)

	client = OpenAI(
		api_key=api_key,
		base_url="https://api.groq.com/openai/v1",
	)

	try:
		response = client.responses.create(
			model="openai/gpt-oss-20b",
			input=prompt,
		)
		return response.output_text
	except Exception as exc:
		raise RuntimeError(f"Groq request failed: {exc}") from exc


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "tour-secret-key")
_storage_ready = False


@app.before_request
def init_storage() -> None:
	global _storage_ready
	if not _storage_ready:
		ensure_storage()
		_storage_ready = True


@app.route("/health", methods=["GET"])
def health() -> Any:
	return jsonify({"status": "ok"})


@app.route("/signup", methods=["POST"])
def signup() -> Any:
	payload = request.json or {}
	username = payload.get("username", "").strip().lower()
	password = payload.get("password", "")

	if not username or not password:
		return jsonify({"error": "Username and password required."}), 400

	users = read_json(USERS_FILE)
	if username in users["users"]:
		return jsonify({"error": "User already exists."}), 400

	users["users"][username] = {
		"password_hash": hash_password(password),
		"created_at": int(time.time()),
	}
	write_json(USERS_FILE, users)

	profiles = read_json(PROFILES_FILE)
	profiles["profiles"][username] = {}
	write_json(PROFILES_FILE, profiles)

	history = read_json(HISTORY_FILE)
	history["history"][username] = []
	write_json(HISTORY_FILE, history)

	favorites = read_json(FAVORITES_FILE)
	favorites["favorites"][username] = []
	write_json(FAVORITES_FILE, favorites)

	return jsonify({"status": "ok"})


@app.route("/login", methods=["POST"])
def login() -> Any:
	payload = request.json or {}
	username = payload.get("username", "").strip().lower()
	password = payload.get("password", "")

	users = read_json(USERS_FILE)
	record = users["users"].get(username)
	if not record or record["password_hash"] != hash_password(password):
		return jsonify({"error": "Invalid credentials."}), 401

	session["username"] = username
	return jsonify({"status": "ok"})


@app.route("/logout", methods=["POST"])
def logout() -> Any:
	session.clear()
	return jsonify({"status": "ok"})


@app.route("/profile", methods=["GET", "PUT"])
def profile() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	profiles = read_json(PROFILES_FILE)
	if request.method == "GET":
		return jsonify(profiles["profiles"].get(username, {}))

	payload = request.json or {}
	profiles["profiles"][username] = {
		"name": payload.get("name", ""),
		"age": payload.get("age", ""),
		"country": payload.get("country", ""),
		"people": payload.get("people", ""),
		"preference": payload.get("preference", ""),
		"weather": payload.get("weather", ""),
		"food": payload.get("food", ""),
	}
	write_json(PROFILES_FILE, profiles)
	return jsonify({"status": "ok"})


@app.route("/recommendations", methods=["POST"])
def recommendations() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	payload = request.json or {}
	user_query = payload.get("query", "")

	local_reply = get_local_response(user_query)
	if local_reply:
		return jsonify({"content": local_reply})

	profiles = read_json(PROFILES_FILE)
	profile = profiles["profiles"].get(username, {})
	prompt = build_prompt(profile, user_query)

	try:
		content = call_groq(prompt)
	except Exception as exc:
		return jsonify({"error": f"AI request failed: {exc}"}), 500

	history = read_json(HISTORY_FILE)
	history["history"].setdefault(username, [])
	history["history"][username].insert(0, {
		"id": str(uuid.uuid4()),
		"timestamp": int(time.time()),
		"query": user_query,
		"response": content,
	})
	history["history"][username] = history["history"][username][:20]
	write_json(HISTORY_FILE, history)

	return jsonify({"content": content})


@app.route("/history", methods=["GET"])
def get_history() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	history = read_json(HISTORY_FILE)
	return jsonify(history["history"].get(username, []))


@app.route("/favorites", methods=["GET", "POST", "DELETE"])
def favorites() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	favorites = read_json(FAVORITES_FILE)
	favorites["favorites"].setdefault(username, [])

	if request.method == "GET":
		return jsonify(favorites["favorites"][username])

	if request.method == "POST":
		payload = request.json or {}
		favorites["favorites"][username].append({
			"id": str(uuid.uuid4()),
			"title": payload.get("title", "Favorite"),
			"details": payload.get("details", ""),
		})
		write_json(FAVORITES_FILE, favorites)
		return jsonify({"status": "ok"})

	payload = request.json or {}
	remove_id = payload.get("id", "")
	favorites["favorites"][username] = [
		item for item in favorites["favorites"][username]
		if item["id"] != remove_id
	]
	write_json(FAVORITES_FILE, favorites)
	return jsonify({"status": "ok"})


@app.route("/itinerary", methods=["POST"])
def itinerary() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	payload = request.json or {}
	days = payload.get("days", 3)
	theme = payload.get("theme", "balanced")

	profiles = read_json(PROFILES_FILE)
	profile = profiles["profiles"].get(username, {})
	prompt = (
		"Create a day-wise travel itinerary. "
		f"Days={days}. Theme={theme}. "
		"Format strictly as: Day 1: bullets, Day 2: bullets, etc. "
		f"Profile: {profile}."
	)

	try:
		content = call_groq(prompt)
	except Exception as exc:
		return jsonify({"error": f"AI request failed: {exc}"}), 500

	return jsonify({"content": content})


@app.route("/search", methods=["GET"])
def search() -> Any:
	try:
		username = require_login()
	except PermissionError:
		return jsonify({"error": "Not authenticated."}), 401

	keyword = request.args.get("q", "").strip().lower()
	history = read_json(HISTORY_FILE)
	items = history["history"].get(username, [])
	if not keyword:
		return jsonify(items)

	filtered = [item for item in items if keyword in item.get("query", "").lower()]
	return jsonify(filtered)


if __name__ == "__main__":
	ensure_storage()
	app.run(host="127.0.0.1", port=5000, debug=False)
