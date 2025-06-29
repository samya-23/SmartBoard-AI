# 🧠 SmartBoard AI – AI-Powered Python Board Game

An interactive turn-based strategy game featuring a smart AI opponent that predicts optimal moves using recursive logic.  
Built using Python and Tkinter, it visualizes live gameplay and supports player elimination on a dynamic tile board.

---

## 🚀 Features

- ♻️ **Circular & Doubly Linked List** to manage board tiles and player turns  
- 🧠 **Recursive AI Bot** that simulates moves ahead to select the best strategy  
- 🎮 **Turn-Based Game Flow** with automatic elimination of jumped players  
- 🖥️ **Tkinter GUI** to display real-time board state and animations  
- 🔁 **Restart Support** and dynamic updates after each move  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **GUI:** Tkinter  
- **Core Concepts:** Object-Oriented Programming, Recursion, Linked Lists  

---

## 📂 Project Structure

```
├── game.py          # Main game logic
├── ai_bot.py        # AI player logic
├── board.py         # Tile and board structure
├── player.py        # Player and PlayerList classes
├── gui_main.py      # Tkinter GUI main app
├── gui_view.py      # Board rendering
├── main.py          # CLI simulation for quick testing
```

---

## 🧠 How AI Works

The AI evaluates all valid jumps and recursively simulates future moves (depth = 2).
Each path is scored based on how many players it can eliminate, and the AI chooses the optimal route.

---

## ✅ Run Locally

```bash
git clone https://github.com/samya-23/SmartBoard-AI.git
cd SmartBoard-AI
python gui_main.py
```

> ✅ Make sure Python and Tkinter are installed.

---

