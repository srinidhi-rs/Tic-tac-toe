# 🧠 Tic-Tac-Toe with Minimax AI

A Python implementation of the classic Tic-Tac-Toe game featuring an **unbeatable AI opponent** powered by the **Minimax algorithm**. This project demonstrates core principles of game theory, recursion, and decision trees in an easy-to-understand format.

---

## 🎮 Features

- ✅ Play as **X** against an intelligent AI (**O**)
- 🧠 AI uses the **Minimax algorithm** to make optimal moves
- 📦 Command-line interface (CLI)
- 🔁 Infinite replayability with draw/win detection

---

## 🧠 How the Minimax Algorithm Works

Minimax is a decision rule for minimizing the possible loss in a worst-case scenario. It simulates all future game states to choose the best move:

- **Maximizer (AI):** Chooses the move with the **highest** score.
- **Minimizer (Human):** Chooses the move with the **lowest** score.
- Scores:
  - `+1`: AI wins
  - `-1`: Human wins
  - `0`: Draw

The algorithm evaluates every possible move recursively to ensure the AI never loses.
