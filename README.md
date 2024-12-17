# Quizzler App

The **Quizzler App** is a True/False quiz game that uses Python and a simple GUI built with `tkinter`. The trivia questions are fetched from the [Open Trivia Database API](https://opentdb.com/), and the app tracks the user's score as they progress.

---

## About the Code

### 1. `main.py`
- The main entry point of the application.
- Initializes the quiz questions, the `QuizBrain` logic, and the `QuizInterface` for the GUI.

### 2. `question_model.py`
- Contains the `Question` class.
- Each `Question` object has:
  - `text`: The trivia question.
  - `answer`: The correct answer (True/False).

### 3. `data.py`
- Fetches trivia questions using the Open Trivia Database API.
- Parses the JSON response to get the question text and correct answer.

### 4. `quiz_brain.py`
- Core logic for managing the quiz:
  - Tracks the current question and user score.
  - Checks if questions are remaining.
  - Decodes HTML entities in question text (e.g., `&quot;` -> `"`).

### 5. `ui.py`
- Builds the graphical interface for the quiz using `tkinter`.
- Features include:
  - Displaying trivia questions.
  - Buttons for True/False answers.
  - Feedback with color-coded backgrounds (green for correct, red for incorrect).
  - Dynamic score updates.

---

## How It Works
1. The app fetches 10 True/False questions from the API.
2. Users answer by clicking the **True** or **False** button.
3. After each question:
   - Feedback is given (background color changes briefly).
   - The next question is displayed.
4. The game ends when all questions are answered, and the final score is shown.

---

## Key Features
- **Dynamic Question Fetching**: Uses an API to fetch new questions each time the app runs.
- **Interactive Feedback**: Visual feedback for correct/incorrect answers.
- **Score Tracking**: Updates the score after every question.

---

Feel free to explore the code and customize it to add more features or improve the design!
