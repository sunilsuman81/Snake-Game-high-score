# Snake Game with High Score Tracking

A classic Snake game built with Python `turtle`.  
The game prompts for player name at startup, stores the highest score in `data.txt`, and appends per-round score history entries (`name : points`) to `record.txt`.

## Features

- Real-time snake movement using arrow keys
- Player name input before gameplay starts
- Food spawning at random coordinates
- Collision detection for:
  - walls
  - snake tail
- Automatic snake reset after collision (instead of closing game)
- Persistent high score saved across runs
- Score history logging with player name and points after each game-over round

## Technical Details

- **Language:** Python
- **Graphics Library:** `turtle` (standard library)
- **Core Modules:**
  - `main.py` -> startup player-name prompt, game loop, event binding, collision checks
  - `snake.py` -> snake body creation, movement, direction control, reset
  - `food.py` -> food object and random repositioning
  - `scoreboard.py` -> score rendering, high-score persistence, per-round record logging (`name : score`)
- **Data Files:**
  - `data.txt` -> stores the current high score
  - `record.txt` -> appends each completed round score with player name

## Game Flow Chart

```mermaid
flowchart TD
    A[Start Program] --> B[Create Screen]
    B --> C[Prompt Player Name]
    C --> D[Create Snake, Food, Scoreboard]
    D --> E[Bind Arrow Keys]
    E --> F[Game Loop]
    F --> G[Move Snake]
    G --> H{Food Collision?}
    H -- Yes --> I[Refresh Food]
    I --> J[Extend Snake]
    J --> K[Increase Score]
    K --> L{Wall or Tail Collision?}
    H -- No --> L
    L -- Yes --> M[Append name : score to record.txt]
    M --> N{New High Score?}
    N -- Yes --> O[Update data.txt]
    N -- No --> P[Reset Score]
    O --> P
    P --> Q[Reset Snake]
    Q --> F
    L -- No --> F
```

## Python Version

- Recommended: **Python 3.9+**
- Works best with official Python installer from [python.org](https://www.python.org/downloads/) to ensure `tkinter`/`turtle` GUI support.

## How to Run

### 1) Clone the repository

```bash
git clone https://github.com/sunilsuman81/Snake-Game-high-score.git
cd Snake-Game-high-score
```

### 2) Run the game

```bash
python3 main.py
```

If `python3` is not available on your system:

```bash
python main.py
```

## Controls

- `Up Arrow` -> move up
- `Down Arrow` -> move down
- `Left Arrow` -> move left
- `Right Arrow` -> move right

## Player Name Input

- At startup, the game asks for player name in a popup dialog.
- If no name is entered, default value is `Player`.
- That name is used when writing entries to `record.txt`.

## Scoring and Persistence

- Current score increases when snake eats food.
- On collision with wall or tail:
  - current round score is appended to `record.txt` as `player_name : score` (for score > 0)
  - game score resets to `0`
  - if current score is greater than saved high score:
    - `data.txt` is updated with new high score

## Notes

- Keep `data.txt` in numeric format so high score can be parsed correctly.
- The game window closes when you click it after loop exits (`exitonclick()`), though normal gameplay is continuous with reset behavior.
