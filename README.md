# Hangman Game Application (API-Based)

## 📌 Overview
This project is a Python-based Hangman game that generates random words using an external API. Each game session fetches a new word, ensuring dynamic and replayable gameplay. The game visually represents player progress using PNG images that update with each incorrect guess.

## 🎮 How the Game Works
- A random word is fetched from a random words API at the start of the game  
- The player guesses letters one at a time  
- Correct guesses reveal letters in the word  
- Incorrect guesses update the hangman image  
- The game ends when the word is guessed or the hangman is fully drawn  

## 📂 Project Structure
- `hangman.py` – Contains the complete game logic, API integration, and input handling  
- `images/` – PNG files representing different hangman stages  

## 🌐 API Usage
The application uses a random words API to retrieve words dynamically instead of relying on a fixed word list. This keeps the game fresh and unpredictable for every playthrough.

## 🧠 Features
- API-driven word generation  
- Visual hangman stages using images  
- Clear win and loss conditions  
- Simple and interactive terminal-based gameplay  

## 🚀 Objective
The goal of this project is to demonstrate API integration, game logic implementation, and interactive visual feedback using Python.
