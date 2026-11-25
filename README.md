# 💩 Poop Run: City

**Live app:** [paste your Streamlit link here]

## What it does
A silly 3D city game at sunset, played in **third person**: the camera follows behind your character as you walk freely around the city eating poop, upgrading your character, dodging traffic and escaping the police.

| Character | Unlocks at | Speed |
|---|---|---|
| 🙂 Chan | start | normal |
| 😎 Aj | 10 💩 | faster |
| 🤠 TienChai | 25 💩 | even faster |
| 👑 Tom Pearl | 50 💩 | fastest |

- 💩 = 1 point, golden 💩 = 3 points
- **Wanted level ⭐:** every 8 points you get another star. Each star adds a police car 🚓, and the police get faster (up to 5 stars)
- **Traffic 🚗:** normal cars drive around the city and can run you over. Stay on the sidewalk to be safe, and be careful crossing the street!
- **Radar:** the round map in the corner turns with you and shows poop, police and cars
- You have 3 lives

**Who it's for:** anyone who wants a quick, funny game. All characters and places are fictional.

## The AI
The police cars use a **path-finding AI** called breadth-first search (BFS). Every step, it works out how many steps each street square is from you, then drives the police toward you along the shortest route. Extra police cars sometimes take a random turn so they spread out and can cut you off.

## How to play
- **Phone:** drag the joystick under the game. Up = walk forward, left/right = turn. Push it all the way to run.
- **Computer:** click the game, then W/↑ = walk, S/↓ = back, A D/← → = turn, hold Shift to run.
- Press 🎥 (or C) to switch between the third-person camera and the sky camera.

## Files
- `app.py` – the Streamlit page and all the game settings (characters, wanted level, traffic, city map)
- `game.html` – the game itself: 3D graphics (made with the free Three.js library), movement, traffic and the police AI
- `requirements.txt` – what Streamlit Cloud needs to install

## What it can't do (limitations)
- The police chase you but don't plan ambushes on purpose.
- You can't drive cars or go inside buildings.
- The police and traffic still move square by square on the streets (only you walk freely).
- On a computer you must click the game before the keys work.
- Your best score is only saved in your own browser.
- It needs internet to load the 3D library, and older phones may run slowly.
- [Add anything else you found while testing.]

## Team
[Names of group members]
