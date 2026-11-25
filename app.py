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
    {"name": "Aj",        "needs": 10, "face": "😎", "color": "#2a9d8f", "speed_ms": 185},
    {"name": "TienChai",  "needs": 25, "face": "🤠", "color": "#e76f51", "speed_ms": 150},
    {"name": "Tom Pearl", "needs": 50, "face": "👑", "color": "#9b5de5", "speed_ms": 120},
]

LIVES = 3
POOP_ON_MAP = 5            # how many poops are on the map at once
POLICE_SPEED_MS = 300      # police step time at the start (smaller = faster)
POLICE_MIN_SPEED_MS = 140  # police never get faster than this
NEW_POLICE_EVERY = 15      # one more police officer every 15 poops
MAX_POLICE = 4
POLICE_RANDOMNESS = 0.25   # extra officers sometimes wander (0 = always chase)

# The map: "#" is a wall, "." is open ground
MAP = [
    "###################",
    "#........#........#",
    "#.##.###.#.###.##.#",
    "#.................#",
    "#.##.#.#####.#.##.#",
    "#....#...#...#....#",
    "#....###.#.###....#",
    "#.##...........##.#",
    "#.##.#.#####.#.##.#",
    "#....#...#...#....#",
    "#.##.###.#.###.##.#",
    "#........#........#",
    "###################",
]

# =========================================================
#  STREAMLIT PAGE
# =========================================================

st.set_page_config(page_title="Poop Run 3D", page_icon="💩", layout="centered")
st.title("💩 Poop Run 3D")
st.write(
    "Run around the map and eat as much poop as you can. "
    "Eat enough and you upgrade to a faster character. "
    "But watch out: the **AI police** 👮 are chasing you!"
)

st.subheader("Characters")
cols = st.columns(len(CHARACTERS))
for col, c in zip(cols, CHARACTERS):
    col.markdown(f"### {c['face']}\n**{c['name']}**\n\n{c['needs']} 💩")

with st.expander("How to play"):
    st.markdown(
        "- **Computer:** click the game, then use the arrow keys or W A S D.\n"
        "- **Phone:** use the buttons under the game, or swipe on the map.\n"
        "- Press 🎥 (or C) to switch between the chase camera and the bird's-eye view.\n"
        "- Eat 💩 to score. You have 3 lives. If the police catch you, you lose one.\n"
        "- The police use a path-finding AI (breadth-first search) to find the "
        "shortest way to you. More police join as you eat more."
    )

config = {
    "characters": CHARACTERS,
    "lives": LIVES,
    "poop_on_map": POOP_ON_MAP,
    "police_speed_ms": POLICE_SPEED_MS,
    "police_min_speed_ms": POLICE_MIN_SPEED_MS,
    "new_police_every": NEW_POLICE_EVERY,
    "max_police": MAX_POLICE,
    "police_randomness": POLICE_RANDOMNESS,
    "map": MAP,
}

with open("game.html", "r", encoding="utf-8") as f:
    game_html = f.read().replace("__CONFIG__", json.dumps(config))

components.html(game_html, height=680, scrolling=False)

st.caption("A silly school practice project. All characters are fictional.")
