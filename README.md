# 🐍 Quiz App - Day 34

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/krishpatel-dev/BasicPy4/graphs/commit-activity)

Welcome to the Quiz App! 🚀 This is a Python-based quiz application that presents true/false questions to users and keeps track of their score. Built with Tkinter for the GUI, this app fetches questions from an API and provides an interactive quiz experience.

## 📋 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)

## ✨ Features

- **Interactive GUI** built with Tkinter
- **True/False Quiz** format
- **Score Tracking** throughout the quiz
- **Responsive Design** that provides feedback on answers
- **Dynamic Question Loading** from an external API
- **Clean and Modern UI** with a consistent color scheme

## 📁 Project Structure

```
Day 34/
├── Proj34_quizzler_app.py  # Main application entry point
├── question_model.py       # Question data model
├── quiz_brain.py          # Quiz logic and scoring
├── ui.py                  # GUI implementation
├── data.py                # Question data handling
└── images/                # Contains UI assets
    ├── true.png
    └── false.png
```

## 🛠 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of Python and OOP concepts

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   (Note: If you don't have a requirements.txt, you can install the required packages manually)

### Running the App

Run the main application file:
```bash
python Proj34_quizzler_app.py
```

## 🧠 How It Works

1. The application starts by loading questions from the Open Trivia Database API
2. The `QuizBrain` class handles the quiz logic, including:
   - Keeping track of the current question
   - Checking answers
   - Calculating scores
3. The `QuizInterface` class manages the GUI components:
   - Displays questions and possible answers
   - Updates the score in real-time
   - Provides visual feedback for correct/incorrect answers

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<div align="center">
  Made with ❤️ and ☕ by <b>Krish</b>
</div>
