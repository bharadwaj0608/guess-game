# 🎯 Number Guessing Game (Python)

A simple command-line Number Guessing Game built using Python. The computer randomly selects a number between **0 and 100**, and the player tries to guess it. The program provides hints after each guess until the correct number is found.

---

## 📌 Features

- Randomly generates a number between **0 and 100**.
- Gives hints:
  - **"Smaller"** if the guessed number is too high.
  - **"Bigger"** if the guessed number is too low.
- Handles invalid inputs using exception handling.
- Prevents the program from crashing when non-numeric input is entered.
- Allows the user to keep guessing until the correct number is found.

---

## 🛠️ Technologies Used

- Python 3.x
- `random` module

---

## 📂 Project Structure

```
Number-Guessing-Game/
│
├── guessing_game.py
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

### 2. Navigate to the project folder

```bash
cd Number-Guessing-Game
```

### 3. Run the program

```bash
python guessing_game.py
```

---

## 🎮 Example Output

```
Enter number 50
Smaller

Enter number 25
Bigger

Enter number 37
Bigger

Enter number 43
You won
```

---

## ⚠️ Exception Handling

The program handles the following exceptions:

- `ValueError` – When the user enters a non-integer value.
- `KeyboardInterrupt` – When the user presses `Ctrl + C`.

If an invalid input is provided, the program displays:

```
Please give valid input
```

---

## 🧠 How It Works

1. The computer randomly generates a number between **0 and 100**.
2. The user enters a guess.
3. The program compares the guess with the generated number.
4. If the guess is:
   - Greater → Displays **"Smaller"**
   - Smaller → Displays **"Bigger"**
   - Equal → Displays **"You won"** and ends the game.
5. The process repeats until the correct number is guessed.

---

## 📖 Concepts Used

- Variables
- Loops (`while`)
- Conditional Statements (`if`, `elif`)
- Exception Handling (`try-except`)
- User Input
- Random Number Generation
- Python Standard Library (`random`)

---

## 🔮 Future Improvements

- Count the number of attempts.
- Add difficulty levels (Easy, Medium, Hard).
- Allow replay without restarting the program.
- Display previous guesses.
- Limit the number of attempts.
- Add a scoring system.
- Provide a graphical user interface (GUI).

---

## 👨‍💻 Author

Developed using Python as a beginner-friendly project to practice:
- Python fundamentals
- Loops
- Conditional logic
- Exception handling
- Random number generation

---

## 📄 License

This project is open source and available under the **MIT License**.