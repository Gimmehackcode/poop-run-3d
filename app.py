import base64
import json
import os
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
#  GAME SETTINGS  (change these to tweak the game!)
# =========================================================

# Ranks: you unlock the next one when you've eaten "needs" poops.
# speed_ms = milliseconds to RUN one map square (smaller = faster). Walking is slower.
# image = the picture shown in the rank box (put the file next to app.py)
CHARACTERS = [
    {"name": "Chan",      "needs": 0,  "color": "#f4a261", "speed_ms": 600, "image": "rank-chan.jpg"},
    {"name": "Aj",        "needs": 10, "color": "#2a9d8f", "speed_ms": 540, "image": "rank-aj.jpg"},
    {"name": "TienChai",  "needs": 25, "color": "#e76f51", "speed_ms": 480, "image": "rank-tienchai.jpg"},
    {"name": "Tom Pearl", "needs": 50, "color": "#ffd23f", "speed_ms": 420, "image": "rank-tompearl.jpg"},
]

# The boss you fight in the Colosseum after you find the 3 question marks (they appear when you reach the last rank)
# hp = how much damage he can take (the Family Member Gun does 1 per bullet, the RPG does 60)
BOSS = {"name": "David", "hp": 260, "image": "boss-david.jpg"}

LIVES = 3
POOP_ON_MAP = 24           # how many poops are in the city at once
GOLDEN_CHANCE = 0.15       # chance a new poop is golden (worth 3!)

# Wanted level: one more police officer every few points
POOP_PER_STAR = 8
MAX_STARS = 5
POLICE_SPEED_MS = 760      # how fast the police run at 1 star (smaller = faster)
POLICE_SPEED_STEP = 65     # police get this much faster per extra star
POLICE_RANDOMNESS = 0.25   # extra officers sometimes take a different street

TRAFFIC_CARS = 16          # cars driving around (they can run you over!)
CAR_SPEED_MS = 520
PEDESTRIANS = 12           # people walking on the sidewalks (just for fun)

# The city map (each character is one square):
#   "#" buildings  "." road  "g" grass  "T" tree  "p" plaza  "k" parking lot
#   "o" pond  "s" sand  "w" sea  "d" pier
# Two roads side by side make a big two-lane avenue.
MAP = [
    "#############################################",
    "#...........................................#",
    "#.####.###.##.#.#####..#####.####.#########.#",
    "#.####.###.##.#.#####..#####.####.#########.#",
    "#.####.###.##.#.#####..#####.####.#########.#",
    "#.................................#########.#",
    "#.ggTg.###.####.#####..#####.####.#########.#",
    "#.gTgg.###.####.#####..#####.####.#########.#",
    "#.gggT.###.####.#####..#####.####.#########.#",
    "#.Tggg.###.####.#####..#####.####.#########.#",
    "#...........................................#",
    "#...........................................#",
    "#.####.###.####.ppppp..#####.####.####.#.##.#",
    "#.####.###.####.ppppp..#####.####.####.#.##.#",
    "#.####.###.####.ppppp..#####.####.####.#.##.#",
    "#.####.###.####.ppppp..#####.####.####.#.##.#",
    "#...........................................#",
    "#.####.########.#####..TgggT.####.kkkk.####.#",
    "#.####.########.#####..ggoog.####.kkkk.####.#",
    "#......########.#####..gToog.####.kkkk.####.#",
    "#.####.########.#####..ggoog.####.kkkk.####.#",
    "#.####.########.#####..TgggT.####.kkkk.####.#",
    "#...........................................#",
    "#.####.###.####.#####..#####.####.####.####.#",
    "#.####.###.####.#####..#####......####.####.#",
    "#.####.###.####.#####..#####.####.####.####.#",
    "#.####.###.####.#####..#####.####.####.####.#",
    "#...........................................#",
    "sssssssssssssssssssssssssssssssssssssssssssss",
    "sssssssssssssssssssssssssssssssssssssssssssss",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwddwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwddwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwddwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwddwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwddwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]

START = [19, 15]   # where you start (column, row) - in the plaza, away from traffic
CITY_SEED = 7      # change this number to get different buildings

# =========================================================
#  STREAMLIT PAGE
# =========================================================

st.set_page_config(page_title="Poop Run: City", page_icon="💩", layout="wide")
st.markdown("### 💩 Poop Run: City")

def picture(path):
    """Turn a picture file into text the game can show (or None if the file is missing)."""
    if not path or not os.path.exists(path):
        return None
    kind = "png" if path.lower().endswith(".png") else "jpeg"
    with open(path, "rb") as f:
        return "data:image/" + kind + ";base64," + base64.b64encode(f.read()).decode()


characters = [{**c, "image": picture(c.get("image"))} for c in CHARACTERS]

config = {
    "characters": characters,
    "boss": {**BOSS, "image": picture(BOSS["image"])},
    "lives": LIVES,
    "poop_on_map": POOP_ON_MAP,
    "golden_chance": GOLDEN_CHANCE,
    "poop_per_star": POOP_PER_STAR,
    "max_stars": MAX_STARS,
    "police_speed_ms": POLICE_SPEED_MS,
    "police_speed_step": POLICE_SPEED_STEP,
    "police_randomness": POLICE_RANDOMNESS,
    "traffic_cars": TRAFFIC_CARS,
    "car_speed_ms": CAR_SPEED_MS,
    "pedestrians": PEDESTRIANS,
    "map": MAP,
    "start": START,
    "seed": CITY_SEED,
}

with open("game.html", "r", encoding="utf-8") as f:
    game_html = f.read().replace("__CONFIG__", json.dumps(config))

components.html(game_html, height=760, scrolling=False)

st.caption(
    "Press ⛶ (or F) in the game for full screen. Move: W A S D · Run: Shift · Look around: hold right mouse button · "
    "Menu: Esc. A silly school practice project - all characters and places are fictional."
)
