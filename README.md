# 🎯 Hangman: Interactive Random Word Guessing Game (API-Based)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Live-brightgreen.svg)

**A modern twist on the classic word game with dynamic difficulty and real-time API integration**

[🎮 Play Live Demo](https://ferwwg5p3vfqmzjy72lldc.streamlit.app/) • [Features](#-features) • [Installation](#-installation) • [How to Play](#-how-to-play)

</div>

---

## 📖 Overview

**Hangman** is an interactive web-based word guessing game built with Streamlit that brings the classic pen-and-paper game into the digital age. Unlike traditional hangman games with static word lists, this version fetches **random words dynamically** from an external API, ensuring every game is unique and unpredictable!

### 🌟 What Makes It Special?

- **🎲 Dynamic Word Generation** - Fresh random words via API, never the same game twice
- **🎚️ Adjustable Difficulty** - Choose word length from 3 to 9 letters
- **🎨 Custom Visual Feedback** - Hand-crafted hangman illustrations for each stage
- **⚡ Real-time Updates** - Instant letter validation and game state management
- **📱 Responsive Design** - Play on desktop, tablet, or mobile
- **🔤 Interactive Keyboard** - Click letters instead of typing for smooth gameplay

---

## ✨ Features

### 🎮 Gameplay Features
- **Smart Word Selection**: Words fetched from Random Word API with customizable length
- **Visual Progress Tracking**: 7 unique hangman stages (0-6 wrong guesses)
- **Disabled Letter Buttons**: Already guessed letters are disabled to prevent confusion
- **Win/Loss Detection**: Automatic game-over detection with celebratory or sympathetic messages
- **Instant Reset**: Start a new game anytime with one click

### 🛠️ Technical Features
- **API Integration**: Real-time word fetching from `random-word-api.vercel.app`
- **Session State Management**: Persistent game state across interactions
- **Clean UI/UX**: Minimalist design focused on gameplay
- **Error Handling**: Graceful degradation if images fail to load
- **Responsive Layout**: Adapts to different screen sizes

---

## 🎥 Demo

### 🎬 Live Application
**👉 [Play Now on Streamlit Cloud](https://ferwwg5p3vfqmzjy72lldc.streamlit.app/)**

### 📸 Screenshots

<div align="center">

| Starting Fresh | Mid-Game Progress | Victory! |
|:-------------:|:-----------------:|:--------:|
| ![Start](https://raw.githubusercontent.com/Maulik1430/Hang-man-game-application-API-based-/main/hangman_0.png) | ![Progress](https://raw.githubusercontent.com/Maulik1430/Hang-man-game-application-API-based-/main/hangman_3.png) | ![Win](https://raw.githubusercontent.com/Maulik1430/Hang-man-game-application-API-based-/main/hangman_0.png) |

</div>

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection (for API calls)

### Quick Start

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Maulik1430/Hang-man-game-application-API-based-.git
cd Hang-man-game-application-API-based-
```

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
```txt
streamlit>=1.28.0
requests>=2.31.0
```

#### 3️⃣ Run the Application
```bash
streamlit run hangman.py
```

The game will open in your default browser at `http://localhost:8501`

---

## 🎮 How to Play

### Game Rules
The classic hangman rules apply:
1. A random word is selected (you choose the length)
2. You see blank spaces representing each letter
3. Guess letters one at a time by clicking the alphabet buttons
4. Correct guesses reveal the letter's position(s)
5. Wrong guesses add a body part to the hangman
6. Win by completing the word before 6 wrong guesses
7. Lose if the hangman is fully drawn (6 mistakes)

### Step-by-Step Guide

**🎚️ Step 1: Set Difficulty**
- Use the slider to choose word length (3-9 letters)
- Shorter words = Easier | Longer words = Harder

**🔤 Step 2: Guess Letters**
- Click any letter button to make a guess
- Guessed letters become disabled (gray)
- Watch the hangman drawing and word progress

**🏆 Step 3: Win or Learn**
- Complete the word to win! 🎉
- If you lose, the word is revealed 💀

**🔁 Step 4: Play Again**
- Click "🔁 New Game" to start fresh
- Adjust difficulty and try again!

---

## 🏗️ Project Structure

```
Hang-man-game-application-API-based-/
│
├── 📄 hangman.py                     # Main application file
│
├── 🖼️ hangman_0.png                  # Hangman stage 0 (empty gallows)
├── 🖼️ hangman_1.png                  # Hangman stage 1 (head)
├── 🖼️ hangman_2.png                  # Hangman stage 2 (body)
├── 🖼️ hangman_3.png                  # Hangman stage 3 (left arm)
├── 🖼️ hangman_4.png                  # Hangman stage 4 (right arm)
├── 🖼️ hangman_5.png                  # Hangman stage 5 (left leg)
├── 🖼️ hangman_6.png                  # Hangman stage 6 (right leg - game over!)
│
├── 📄 README.md                      # This file
└── 📄 requirements.txt               # Python dependencies
```

---

## 🧠 How It Works

### 🎲 Random Word Generation

```python
def word_lookup(length):
    url = f"https://random-word-api.vercel.app/api?words=1&type=uppercase&length={length}"
    res = requests.get(url)
    return res.json()[0]
```

**API Endpoint:** `random-word-api.vercel.app`
- Fetches a single random word
- Filters by exact length (3-9 characters)
- Returns uppercase for consistency

### 🎨 Visual Feedback System

```python
def get_image_url(wrong_count):
    return f"{BASE_IMG_URL}/hangman_{wrong_count}.png"
```

**Image Progression:**
- `hangman_0.png` → Empty gallows (fresh start)
- `hangman_1.png` → Head appears (1st mistake)
- `hangman_2.png` → Body added (2nd mistake)
- `hangman_3.png` → Left arm (3rd mistake)
- `hangman_4.png` → Right arm (4th mistake)
- `hangman_5.png` → Left leg (5th mistake)
- `hangman_6.png` → Right leg (6th mistake - GAME OVER)

All images are **custom-designed** and hosted on GitHub for fast loading!

### 💾 Session State Management

```python
st.session_state = {
    "word": "PYTHON",           # Current target word
    "guessed": ["P", "Y"],      # Letters already guessed
    "wrong": 2,                  # Number of mistakes
    "game_over": False           # Game status flag
}
```

Streamlit's session state keeps track of:
- Current word being guessed
- All guessed letters (to disable buttons)
- Wrong guess count (for image updates)
- Game over status (to freeze gameplay)

---

## 🎨 Customization

### Change Difficulty Range
```python
# In hangman.py, modify the slider range
length = st.slider("Word Length", 3, 12, 5)  # Now goes up to 12 letters!
```

### Adjust Maximum Wrong Guesses
```python
# Change MAX_WRONG to make it easier/harder
MAX_WRONG = 8  # Allows 8 mistakes instead of 6
```

### Add More Hangman Stages
1. Create new images: `hangman_7.png`, `hangman_8.png`, etc.
2. Update `MAX_WRONG` constant
3. Upload images to your GitHub repository

### Use Custom Word Lists
Replace the API call with your own word list:
```python
import random

def word_lookup(length):
    words = ["PYTHON", "STREAMLIT", "HANGMAN", "CODING"]
    return random.choice([w for w in words if len(w) == length])
```

---

## 🛠️ Technical Details

### Technologies Used
| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web framework for interactive UI |
| **Requests** | HTTP library for API calls |
| **Random Word API** | Dynamic word generation |

### Key Libraries
```python
import streamlit as st      # UI framework
import requests             # API requests
import string               # Alphabet generation
```

### Performance Optimization
- ✅ **Session state** prevents unnecessary re-fetches
- ✅ **Image caching** via GitHub CDN
- ✅ **Efficient rerendering** using `st.rerun()`
- ✅ **Lazy loading** - API called only when needed

---

## 🎓 Learning Outcomes

Building this project teaches:
- 📡 **API Integration** - Fetching and parsing JSON data
- 🔄 **State Management** - Handling session state in Streamlit
- 🎨 **UI/UX Design** - Creating intuitive game interfaces
- 🐛 **Error Handling** - Graceful degradation when resources fail
- 🎮 **Game Logic** - Win/loss detection and flow control

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas to enhance the game:

### 🌟 Feature Ideas
- [ ] Add difficulty modes (easy/medium/hard word categories)
- [ ] Implement hint system (reveal one random letter)
- [ ] Add sound effects for correct/wrong guesses
- [ ] Create leaderboard with localStorage
- [ ] Add multiplayer mode (two players take turns)
- [ ] Include word definitions (using Dictionary API)
- [ ] Add timer for speed challenges
- [ ] Theme customization (dark mode, color schemes)

### Steps to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙋 FAQ

**Q: What happens if the API is down?**  
A: The game will display "ERROR" as the word. Consider adding a fallback word list for offline play.

**Q: Can I use my own images?**  
A: Absolutely! Replace the `hangman_X.png` files in your repository and update the `BASE_IMG_URL` in the code.

**Q: Why does the game reset when I change the word length?**  
A: The slider triggers a new game initialization to ensure the word matches your selected length.

**Q: Can I deploy this on platforms other than Streamlit Cloud?**  
A: Yes! You can deploy on Heroku, AWS, Google Cloud, or any platform that supports Python web apps.

**Q: How do I add hints?**  
A: You can add a "Reveal Hint" button that reveals one random unrevealed letter:
```python
if st.button("💡 Hint"):
    unrevealed = [c for c in word if c not in st.session_state["guessed"]]
    if unrevealed:
        st.session_state["guessed"].append(random.choice(unrevealed))
        st.rerun()
```

**Q: Is there a way to track high scores?**  
A: Currently, no. But you could implement this using Streamlit's `st.experimental_get_query_params()` or integrate a database like SQLite or Firebase.

---

## 🌟 Acknowledgments

- **Random Word API** - [random-word-api.vercel.app](https://random-word-api.vercel.app/) for providing free random words
- **Streamlit** - For the amazing framework that makes building web apps effortless
- **Custom Artwork** - All hangman illustrations designed and created by **Maulik**
- **Classic Game Inspiration** - The timeless word game that has entertained generations

---

## 📧 Contact & Support

**Developer:** Maulik  
**Repository:** [Hang-man-game-application-API-based-](https://github.com/Maulik1430/Hang-man-game-application-API-based-)  
**Live Demo:** [Play on Streamlit Cloud](https://ferwwg5p3vfqmzjy72lldc.streamlit.app/)

### Found a Bug? 🐛
Please open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### Have a Feature Request? 💡
Open an issue with the "enhancement" label and describe:
- What feature you'd like to see
- Why it would be useful
- Any implementation ideas

---

## 🎮 Ready to Play?

<div align="center">

### 🚀 [**Launch the Game Now!**](https://ferwwg5p3vfqmzjy72lldc.streamlit.app/)

**Star ⭐ this repository if you enjoyed playing!**

---

Made with ❤️ and Python by [Maulik](https://github.com/Maulik1430)

*Keep guessing, keep winning!* 🎯

</div>
