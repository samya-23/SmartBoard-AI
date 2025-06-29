<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SmartBoard AI – AI-Powered Python Board Game</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      margin: 40px;
      max-width: 800px;
      color: #333;
    }
    h1, h2, h3 {
      color: #1f3c88;
    }
    code, pre {
      background: #f4f4f4;
      padding: 4px 8px;
      border-radius: 4px;
      font-family: monospace;
    }
    ul {
      padding-left: 20px;
    }
    .screenshot {
      margin: 20px 0;
    }
  </style>
</head>
<body>

<h1>🧠 SmartBoard AI – AI-Powered Python Board Game</h1>

<p>
  An interactive turn-based strategy game featuring a smart AI opponent that predicts optimal moves using recursive logic.
  Built using Python and Tkinter, it visualizes live gameplay and supports player elimination on a dynamic tile board.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>♻️ <strong>Circular & Doubly Linked List</strong> to manage board tiles and player turns</li>
  <li>🧠 <strong>Recursive AI Bot</strong> that simulates moves ahead to select the best strategy</li>
  <li>🎮 <strong>Turn-Based Game Flow</strong> with automatic elimination of jumped players</li>
  <li>🖥️ <strong>Tkinter GUI</strong> to display real-time board state and animations</li>
  <li>🔁 <strong>Restart Support</strong> and dynamic updates after each move</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><strong>Language</strong>: Python</li>
  <li><strong>GUI</strong>: Tkinter</li>
  <li><strong>Core Concepts</strong>: Object-Oriented Programming, Recursion, Linked Lists</li>
</ul>

<hr>

<h2>📸 Screenshots</h2>
<div class="screenshot">
  <em>(Add screenshots here)</em><br>
  <code>&lt;img src="screenshots/game.png" alt="Game Screenshot" width="600"&gt;</code>
</div>

<hr>

<h2>📂 Project Structure</h2>
<pre><code>
├── game.py          # Main game logic
├── ai_bot.py        # AI player logic
├── board.py         # Tile and board structure
├── player.py        # Player and PlayerList classes
├── gui_main.py      # Tkinter GUI main app
├── gui_view.py      # Board rendering
├── main.py          # CLI simulation for quick testing
</code></pre>

<hr>

<h2>🧠 How AI Works</h2>
<p>
  The AI evaluates all valid jumps and recursively simulates future moves (depth = 2).
  Each path is scored based on how many players it can eliminate, and the AI chooses the optimal route.
</p>

<hr>

<h2>✅ Run Locally</h2>
<pre><code>
git clone https://github.com/yourusername/smartboard-ai.git
cd smartboard-ai
python gui_main.py
</code></pre>
<p>Make sure Python and Tkinter are installed.</p>

<hr>

<h2>📌 Credits</h2>
<p>
  Created with ❤️ by <strong>Your Name</strong><br>
  Inspired by board game mechanics and algorithmic decision-making.
</p>

<hr>

<h2>📄 License</h2>
<p>MIT License – feel free to use or modify.</p>

</body>
</html>
