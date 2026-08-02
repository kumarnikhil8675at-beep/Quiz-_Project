# 🧠 Quiz Game (Open Trivia API)

A desktop quiz application built with **Python**, **Tkinter**, and the **Open Trivia Database API**. The application downloads True/False questions from the API, displays them one at a time, checks the user's answers, tracks the score, and provides instant feedback.

---

## 📌 Features

- Fetches live quiz questions from the Open Trivia Database API.
- Displays one question at a time.
- Supports True/False questions.
- Automatically decodes HTML entities.
- Tracks user score.
- Instant answer feedback using color changes.
- Disables answer buttons after the quiz ends.
- Clean and interactive Tkinter GUI.

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Requests
- HTML Module
- Object-Oriented Programming (OOP)

---

## 📁 Project Structure

```
quiz-game/
│
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
├── ui.py
├── images/
│   ├── true.png
│   └── false.png
└── README.md
```

---

## 📂 File Description

### `main.py`
- Creates Question objects.
- Initializes the quiz.
- Starts the graphical interface.

### `data.py`
- Fetches quiz questions from the Open Trivia Database API.

### `question_model.py`
- Defines the `Question` class.
- Stores question text and answer.

### `quiz_brain.py`
- Controls quiz logic.
- Manages questions, score, and answer checking.

### `ui.py`
- Builds the Tkinter interface.
- Displays questions.
- Handles button events.
- Updates the interface after each answer.

---

## 🚀 How It Works

1. Requests quiz questions from the Open Trivia Database API.
2. Converts each question into a `Question` object.
3. Stores all questions in the quiz brain.
4. Displays one question at a time.
5. User selects **True** or **False**.
6. Checks whether the answer is correct.
7. Updates the score and loads the next question.
8. Ends the quiz after all questions are answered.

---

## 🌐 API Used

**Open Trivia Database**

```
https://opentdb.com/api.php
```

Example Request:

```
https://opentdb.com/api.php?amount=10&type=boolean
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install requests
```

Run the application:

```bash
python main.py
```

---

## 📚 Concepts Learned

- Python Classes & Objects
- Object-Oriented Programming
- API Integration
- JSON Handling
- Tkinter GUI Development
- Event Handling
- Modular Programming
- HTML Entity Decoding

---

## 🔮 Future Improvements

- Multiple-choice questions
- Difficulty selection
- Category selection
- Timer for each question
- High score system
- Sound effects

Python Quiz Game built using Tkinter and the Open Trivia Database API.
