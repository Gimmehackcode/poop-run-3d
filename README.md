# 💩 Poop Run: City

**Live app:** [paste your Streamlit link here]

## What it does
A silly third-person 3D city game at sunset. Walk and run around a big city with skyscrapers, a park and a beach, eat poop to upgrade your character, stay on the sidewalk to avoid traffic, and escape the police when your wanted level goes up.

It starts with a main menu (Play, Characters, Controls, Settings, Credits). Press Esc during the game for the pause menu.

| Character | Unlocks at |
|---|---|
| Chan | start |
| Aj | 10 💩 |
| TienChai | 25 💩 |
| Tom Pearl | 50 💩 |

- 💩 = 1 point, golden 💩 = 3 points. Each character you unlock runs faster
- **Wanted level ⭐:** every 8 points you get another star. Each star adds a police car 🚓, and the police get faster (up to 5 stars)
- **Traffic 🚗:** cars drive around the city and can run you over. Stay on the sidewalk and be careful crossing the street!
- **Radar:** the round map in the corner turns with the camera and shows poop and police
- You have 3 lives

**Who it's for:** anyone who wants a quick, funny game. All characters and places are fictional.

## The AI
The police cars use a **path-finding AI** called breadth-first search (BFS). Every step, it works out how many steps each street square is from you, then drives the police toward you along the shortest route. Extra police cars sometimes take a random turn so they spread out and can cut you off.

## Controls
- **Move:** W A S D or arrow keys. You walk the way the camera is facing
- **Run:** hold Shift
- **Look around:** hold the right mouse button and drag
- **Zoom:** mouse wheel · **Camera behind you:** C · **Pause menu:** Esc or P
- **Phone:** joystick under the game to walk (push all the way to run), drag on the game to look around

## Files
- §BT§app.py§BT§ – the Streamlit page and all the game settings (characters, wanted level, traffic, city map)
- §BT§game.html§BT§ – the game itself: 3D graphics (Three.js), menus, movement, camera, traffic and the police AI
- §BT§requirements.txt§BT§ – what Streamlit Cloud needs to install

## Credits
- 3D engine: [Three.js](https://threejs.org)
- Person model: the "Soldier" model from the Three.js examples, with walk/run animations from Mixamo
- Fonts: Bebas Neue and Oswald (Google Fonts)

## What it can't do (limitations)
- The police chase you but don't plan ambushes on purpose.
- You can't drive cars or go inside buildings.
- The police and traffic move square by square along the streets (only you move freely).
- It needs internet to load the 3D library and the person model. If the model can't load, a simple block person is used instead.
- On a computer you must click the game before the keys work.
- Your best score and settings are only saved in your own browser.
- Older phones may run slowly. Set Graphics to Low in Settings if that happens.
- [Add anything else you found while testing.]

## Team
[Names of group members]
