# 💩 Poop Run: City

**Live app:** [paste your Streamlit link here]

## What it does
A silly third-person 3D city game at sunset. Walk and run around a big city with glass skyscrapers, brick apartments, shops, two-lane avenues, a plaza with a fountain, a park with a pond, a parking lot, a beach and a pier. Eat poop to upgrade your character, dodge the traffic, and escape the police officers chasing you on foot when your wanted level goes up. Press ⛶ or F for full screen.

It starts with a main menu (Play, Characters, Controls, Settings, Credits). Press Esc during the game for the pause menu.

The box in the top-left corner shows your current rank picture and how close you are to the next rank. When you rank up, a big pop-up in the middle of the screen says "Congratulations! You've ranked up to ...". Your rank picture is also your character's face.

The police are patrol officers in blue uniforms and caps. From 3 wanted stars, SWAT officers join the chase.

Cars drive in their lanes, stop at traffic lights and brake (and honk!) if you stand in front of them - but they can't stop instantly. When you eat a poop, your character nibbles it like a hamster with puffed-up cheeks, and you can keep running while you eat.

| Character | Unlocks at |
|---|---|
| Chan | start |
| Aj | 10 💩 |
| TienChai | 25 💩 |
| Tom Pearl | 50 💩 |

- 💩 = 1 point, golden 💩 = 3 points. Each character you unlock runs faster
- **Wanted level ⭐:** every 8 points you get another star. Each star adds a police officer 👮 who chases you on foot, and the police get faster (up to 5 stars)
- **Traffic 🚗:** cars drive around the city and can run you over. Stay on the sidewalk and be careful crossing the street!
- **Radar:** the round map in the corner turns with the camera and shows poop and police
- You have 3 lives

**Who it's for:** anyone who wants a quick, funny game. All characters and places are fictional.

## The AI
The police officers use a **path-finding AI** called breadth-first search (BFS). A few times a second it works out how many steps each walkable square is from you, and each officer runs along the shortest route. When an officer is close and can see you, they run straight at you. Extra officers sometimes take a different street so they can cut you off.

## Controls
- **Move:** W A S D or arrow keys. You walk the way the camera is facing
- **Run:** hold Shift
- **Look around:** hold the right mouse button and drag
- **Zoom:** mouse wheel · **Camera behind you:** C · **Full screen:** F · **Pause menu:** Esc or P
- **Phone:** joystick in the bottom corner to walk (push all the way to run), drag on the screen to look around

## Files
- `app.py` – the Streamlit page and all the game settings (characters, wanted level, traffic, city map)
- `game.html` – the game itself: 3D graphics (Three.js), menus, movement, camera, traffic and the police AI
- `requirements.txt` – what Streamlit Cloud needs to install
- `rank-chan.jpg`, `rank-aj.jpg`, `rank-tienchai.jpg`, `rank-tompearl.jpg` – the rank pictures (AI-generated). Swap them for your own pictures with the same names

## Credits
- 3D engine: [Three.js](https://threejs.org)
- People: the "Soldier" (you) and "X Bot" (pedestrians) models from the Three.js examples, with animations from Mixamo
- Patrol officer (`models/police-officer.glb`): made with MakeHuman from its CC0 assets, with animations from Quaternius' Universal Animation Library (CC0), as packaged in the police-command project
- SWAT officer (`models/police-swat.gltf`): "SWAT" by Quaternius (CC0)
- Fonts: Bebas Neue and Oswald (Google Fonts)

## What it can't do (limitations)
- The police chase you but don't plan ambushes on purpose.
- You can't drive cars or go inside buildings.
- Pedestrians just walk around their block and don't cross the road.
- It needs internet to load the 3D library and the people models. If a model can't load, a simple block person is used instead.
- Full screen doesn't work on iPhones (Apple doesn't allow it for web pages).
- On a computer you must click the game before the keys work.
- Your best score and settings are only saved in your own browser.
- Older phones may run slowly. Set Graphics to Low in Settings if that happens.
- [Add anything else you found while testing.]

## Team
[Names of group members]
