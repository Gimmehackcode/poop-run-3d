import json
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
#  GAME SETTINGS  (change these to tweak the game!)
# =========================================================

# Characters unlock when you've eaten "needs" poops.
# speed_ms = how many milliseconds per step (smaller = faster)
CHARACTERS = [
    {"name": "Chan",      "needs": 0,  "face": "🙂", "color": "#f4a261", "speed_ms": 220},
    {"name": "Aj",        "needs": 10, "face": "😎", "color": "#2a9d8f", "speed_ms": 190},
    {"name": "TienChai",  "needs": 25, "face": "🤠", "color": "#e76f51", "speed_ms": 160},
    {"name": "Tom Pearl", "needs": 50, "face": "👑", "color": "#9b5de5", "speed_ms": 130},
]

LIVES = 3
POOP_ON_MAP = 6            # how many poops are in the city at once
GOLDEN_CHANCE = 0.12       # chance a new poop is golden (worth 3!)

# Wanted level: one more star (and one more police car) every few poops
POOP_PER_STAR = 8
MAX_STARS = 5
POLICE_SPEED_MS = 320      # police speed at 1 star (smaller = faster)
POLICE_SPEED_STEP = 25     # police get this much faster per extra star
POLICE_RANDOMNESS = 0.25   # extra police cars sometimes take a random turn

TRAFFIC_CARS = 5           # normal cars driving around (they can run you over!)
CAR_SPEED_MS = 260

# The city map:
#   "#" building   "." road   "g" park grass   "T" park tree   "P" palm tree
MAP = [
    "############################",
    "#..........................#",
    "#.P###.P###.####.#.##.P###.#",
    "#.####.####.####.#.##.####.#",
    "#.####.####.####.#.##.####.#",
    "#.###P.###P.####.#.##.###P.#",
    "#..........................#",
    "#.P###.####.gggg.P###.####.#",
    "#.####.####.gTgg.####......#",
    "#.####.####.ggTg.####.####.#",
    "#.###P.####.gggg.###P.####.#",
    "#..........................#",
    "#.#.##.P###.####.P###.P###.#",
    "#.#.##......####.####.####.#",
    "#.#.##.####.####.####.####.#",
    "#.#.##.###P.####.###P.###P.#",
    "#..........................#",
    "############################",
]

CITY_SEED = 7  # change this number to get different building colours and heights

# =========================================================
#  STREAMLIT PAGE
# =========================================================

st.set_page_config(page_title="Poop Run: City", page_icon="💩", layout="centered")
st.title("💩 Poop Run: City")
st.write(
    "Sunset in the city. Run the streets, eat as much poop as you can and upgrade your character. "
    "The more you eat, the higher your **wanted level** ⭐, and the more **police cars** 🚓 chase you. "
    "Watch out for traffic too!"
)

st.subheader("Characters")
cols = st.columns(len(CHARACTERS))
for col, c in zip(cols, CHARACTERS):
    col.markdown(f"### {c['face']}\n**{c['name']}**\n\n{c['needs']} 💩")

with st.expander("How to play"):
    st.markdown(
        "- **Phone:** drag the joystick under the game. Up = walk forward, left/right = turn. Push it all the way to run.\n"
        "- **Computer:** click the game, then W/↑ = walk, S/↓ = back, A D/← → = turn, hold Shift to run.\n"
        "- The camera follows behind you. Press 🎥 (or C) to switch to the sky camera.\n"
        "- 💩 = 1 point, golden 💩 = 3 points. You have 3 lives.\n"
        "- Police cars catch you, traffic runs you over: both cost a life.\n"
        "- The radar in the corner shows poop (brown/gold), police (flashing) and cars (grey).\n"
        "- The police use a path-finding AI (breadth-first search) to find the "
        "shortest way to you through the streets."
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
    "seed": CITY_SEED,
}

with open("game.html", "r", encoding="utf-8") as f:
    game_html = f.read().replace("__CONFIG__", json.dumps(config))

components.html(game_html, height=680, scrolling=False)

st.caption("A silly school practice project. All characters and places are fictional.")
