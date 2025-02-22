# 🐍 Snake Game

A classic **Snake Game** built with **Python** using the **turtle** graphics library.

---

## 🎮 Features

- Classic snake gameplay with increasing length.
- Food spawning at random positions.
- Scoreboard that tracks your score.
- Game over screen when colliding with walls or itself.

---

## 📂 Project Structure

```
.
├── main.py            # Main game loop
├── snake.py           # Snake class logic
├── food.py            # Food generation logic
├── score_board.py     # Scoreboard display and logic
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

- **Python 3.x** installed.

Check Python version:
```bash
python --version
```

### 2️⃣ Install Dependencies

The game uses Python's built-in **turtle** module, so no external libraries are required.

---

## 🕹️ How to Play

1. **Run the Game:**
   ```bash
   python main.py
   ```

2. **Controls:**
   - **Up Arrow** – Move Up
   - **Down Arrow** – Move Down
   - **Left Arrow** – Move Left
   - **Right Arrow** – Move Right

3. **Objective:**
   - Eat the green food to grow your snake.
   - Avoid hitting the walls or colliding with yourself.
   - Score as high as possible!

4. **End Game:**
   - When the snake hits the wall or itself, the game ends with a **Game Over** screen.

---

## ⚡ Code Overview

- **main.py**: Initializes the game screen and handles the game loop.
- **snake.py**: Manages snake movement, direction changes, and collisions.
- **food.py**: Generates food at random positions on the screen.
- **score_board.py**: Tracks and displays the player's score.

