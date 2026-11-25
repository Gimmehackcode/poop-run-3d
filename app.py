import json
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
#  GAME SETTINGS  (change these to tweak the game!)
# =========================================================

# Characters unlock when you've eaten "needs" poops.
# speed_ms = milliseconds to RUN one map square (smaller = faster). Walking is slower.
CHARACTERS = [
    {"name": "Chan",      "needs": 0,  "color": "#f4a261", "speed_ms": 520},
    {"name": "Aj",        "needs": 10, "color": "#2a9d8f", "speed_ms": 470},
    {"name": "TienChai",  "needs": 25, "color": "#e76f51", "speed_ms": 420},
    {"name": "Tom Pearl", "needs": 50, "color": "#ffd23f", "speed_ms": 370},
]

LIVES = 3
POOP_ON_MAP = 12           # how many poops are in the city at once
GOLDEN_CHANCE = 0.12       # chance a new poop is golden (worth 3!)

# Wanted level: one more star (and one more police car) every few points
POOP_PER_STAR = 8
MAX_STARS = 5
POLICE_SPEED_MS = 680      # police speed at 1 star (smaller = faster)
POLICE_SPEED_STEP = 55     # police get this much faster per extra star
POLICE_RANDOMNESS = 0.25   # extra police cars sometimes take a random turn

TRAFFIC_CARS = 14          # normal cars driving around (they can run you over!)
CAR_SPEED_MS = 480

# The city map (each character is one square):
#   "#" buildings   "." road   "g" park grass   "T" park tree   "s" sand   "w" sea
# Buildings in the middle of the map are skyscrapers, the edges are lower.
MAP = [
    "###########################################",
    "#.........................................#",
    "#.####.####.##.#.####.####.####.####.####.#",
    "#.####.####.##.#.####.####.####.####.####.#",
    "#.####.####.##.#.####.####.####.####.####.#",
    "#.####.####.##.#.####.####.####.####.####.#",
    "#.........................................#",
    "#.####.####.####.####.####.####.####.####.#",
    "#.####.####.####.####.####......####.####.#",
    "#.####.####.####.####.####.####.####.####.#",
    "#.####.####.####.####.####.####.####.####.#",
    "#.........................................#",
    "#.####.####.####.gggT.####.####.####.####.#",
    "#.####.####.####.gTgg.####.####.####......#",
    "#.####.####.####.gggg.####.####.####.####.#",
    "#.####.####.####.TgTg.####.####.####.####.#",
    "#.........................................#",
    "#.####.##.#.####.####.####.####.gTgg.####.#",
    "#......##.#.####.####.####.####.gggT.####.#",
    "#.####.##.#.####.####.####.####.gggg.####.#",
    "#.####.##.#.####.####.####.####.ggTg.####.#",
    "#.........................................#",
    "#.####.####.####.####.##.#.####.####.####.#",
    "#.####.####.####.####.##.#.####.####.####.#",
    "#.####.####.####.####.##.#.####.####.####.#",
    "#.####.####.####.####.##.#.####.####.####.#",
    "#.........................................#",
    "sssssssssssssssssssssssssssssssssssssssssss",
    "sssssssssssssssssssssssssssssssssssssssssss",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]

START = [21, 16]   # where you start (column, row) - must be a road square
CITY_SEED = 7      # change this number to get different building colours and heights

# =========================================================
#  STREAMLIT PAGE
# =========================================================

st.set_page_config(page_title="Poop Run: City", page_icon="💩", layout="centered")
st.title("💩 Poop Run: City")
st.write(
    "A third-person city game at sunset. Walk and run around the city, eat poop to upgrade your character, "
    "stay on the sidewalk to avoid traffic, and escape the police when your **wanted level** ⭐ goes up."
)

config = {
    "characters": CHARACTERS,
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
    "map": MAP,
    "start": START,
    "seed": CITY_SEED,
}

with open("game.html", "r", encoding="utf-8") as f:
    game_html = f.read().replace("__CONFIG__", json.dumps(config))

components.html(game_html, height=600, scrolling=False)

with st.expander("Controls"):
    st.markdown(
        "- **Move:** W A S D or arrow keys (phone: joystick under the game)\n"
        "- **Run:** hold Shift (phone: push the joystick all the way)\n"
        "- **Turn the camera:** hold the right mouse button and drag (phone: drag on the game)\n"
        "- **Zoom:** mouse wheel · **Reset camera:** C · **Pause menu:** Esc or P\n"
        "- Click the game first so it can hear your keyboard."
    )

st.caption("A silly school practice project. All characters and places are fictional.")
