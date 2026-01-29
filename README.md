# Mood Tracker ChatBot (Python & Flask)

A simple and interactive web-based chatbot designed to check your daily mood and save journal entries. This project demonstrates basic Natural Language Processing (NLP) concepts and file handling in Python.

## 🚀 Project Overview

The **Mood Tracker ChatBot** allows users to input how they are feeling. The bot analyzes the sentiment of the input, provides a response based on the detected mood, and logs the entry into a persistent journal file.

### Key Features
- **Sentiment Detection**: Analyzes user input to identify positive or negative moods.
- **Journal Logging**: Automatically saves user thoughts to `journal.txt` for future reflection.
- **Web Interface**: A clean UI built with HTML templates for a seamless user experience.
- **Python Backend**: Logic powered by Python (using the Flask framework).

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## 📁 Repository Structure

- `mood.py`: The main Python script containing the Flask application and mood-checking logic.
- `templates/`: Folder containing the HTML frontend files.
- `journal.txt`: A text file used as a lightweight database to store user entries.
- `README.md`: Project documentation.

## 🔧 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ArulSrivastva-AVV/A-Basic-Python-Mood-Checker-ChatBot.git](https://github.com/ArulSrivastva-AVV/A-Basic-Python-Mood-Checker-ChatBot.git)

2. Install Flask:

   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python mood.py
   ```
4. Accessing the ChatBot:
   go to you browser and paste this URL
   ```
   http://127.0.0.1:5000
   ```

