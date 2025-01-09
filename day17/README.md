# 100-days-of-code:day 17
---
# Python Quiz Game

This repository contains a simple, text-based **Quiz Game** built with Python. The project demonstrates core Python concepts such as classes, objects, and loops, and provides an engaging way to test knowledge with a series of True/False questions.

---

## Features

- **Question Bank:** A pre-defined set of True/False questions.
- **Interactive Gameplay:** Users are prompted to answer each question.
- **Score Tracking:** The game keeps track of the user's score.
- **Encapsulation:** Organized code using classes for better modularity and readability.

---

## Files Overview

### `data.py`
Contains the `question_data` list, a collection of dictionaries, each representing a question with its text and correct answer.

Example:
```python
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    ...
]

question_model.py

Defines the Questions class, representing a question with text and an answer.

class Questions:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

quiz_brain.py

Defines the QuizBrain class, which manages the quiz flow:

    Tracks the current question.
    Checks user answers.
    Keeps track of the user's score.

Key methods:

    still_has_questions(): Checks if there are questions left in the quiz.
    next_question(): Presents the next question and processes the user's answer.

main.py

The main driver script that initializes the quiz:

    Converts question_data into Questions objects.
    Runs the quiz in a loop until all questions are answered.
    Displays the final score at the end.

How to Run the Game

    Clone this repository:

git clone https://github.com/your-username/python-quiz-game.git
cd python-quiz-game

Run the main.py file:

    python main.py

    Answer the questions as prompted, typing True or False.

Example Gameplay

Q.1: A slug's blood is green. (True/False): True
You are right!

Q.2: The loudest animal is the African Elephant. (True/False): False
You are right!

... (continues until all questions are answered) ...

You completed the quiz!
Your final score was: 10/12

Concepts Demonstrated

    Object-Oriented Programming: Encapsulation of data and logic into Questions and QuizBrain classes.
    Data Management: Storing and retrieving question data from a list of dictionaries.
    User Interaction: Prompting for and validating user input.


