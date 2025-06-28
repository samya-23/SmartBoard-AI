# Deep Sea Diver 🐙

A Python-based turn-based board game with GUI where players "jump" over others like checkers, implemented using a circular linked list (for players) and doubly linked list (for the board).

---

## 🚀 Features

- ✅ Linked list–based board (not array)
- 🔄 Circular linked list for player turns
- 🧩 "Dancing links"-style player removal (O(1) unlinking)
- 🖥️ GUI with Tkinter — click "Next Move" to play interactively
- 💡 Designed for performance & conceptual elegance

---

## 🧠 Why It's Interesting

Unlike typical game implementations that use arrays, this project is built entirely on **linked data structures**:

- Each tile = node in a **doubly linked list**
- Player turn order = **circular linked list**
- "Jumping" over a player = **unlinking enemy node** (like *dancing links*)

This ensures:
- 🔁 Constant-time moves (O(1) per step)
- 🧠 No array shifts or index management
- 🧼 Clean logic separation between structure & game rules

---

## 🛠️ Requirements

- Python 3.7+
- No third-party libraries required

> 💡 If `tkinter` is missing (common on Linux), install via:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 📦 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/samya-23/deep-sea-diver.git
   cd deep-sea-diver

