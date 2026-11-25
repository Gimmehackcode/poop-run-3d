# 💩 Poop Run 3D

**Live app:** [paste your Streamlit link here]

## What it does
A silly 3D maze game. You run around the map eating poop. Eat enough and your character upgrades:

| Character | Unlocks at | Speed |
|---|---|---|
| 🙂 Chan | start | normal |
| 😎 Aj | 10 💩 | faster |
| 🤠 TienChai | 25 💩 | even faster |
| 👑 Tom Pearl | 50 💩 | fastest |

AI police 👮 chase you. You have 3 lives. Every 15 poops, another officer joins the chase (up to 4).

**Who it's for:** anyone who wants a quick, funny game. All characters are fictional.

## The AI
The police use a **path-finding AI** called breadth-first search (BFS). Every step, it works out how far each square of the map is from you, then moves the police to the square that gets closest. Extra officers sometimes wander randomly so they don't all follow the same path.

## How to play
- **Computer:** click the game, then use the arrow keys or W A S D.
- **Phone:** use the buttons under the game, or swipe on the map.
- Press 🎥 (or C) to switch between the chase camera and the bird's-eye view.

## Files
- `app.py` – the Streamlit page and all the game settings (characters, speeds, map)
- `game.html` – the game itself: 3D graphics (made with the free Three.js library), movement and the police AI
- `requirements.txt` – what Streamlit Cloud needs to install

## What it can't do (limitations)
- The police only chase. They don't plan ahead or trap you on purpose.
- On a computer you must click the game before the keys work.
- Your best score is only saved in your own browser.
- It needs internet to load the 3D library, and very old phones may run it slowly.
- [Add anything else you found while testing.]

## Team
[Names of group members]
