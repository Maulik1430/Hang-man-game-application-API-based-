import streamlit as st
import requests
import string
import random
import time

BASE_IMG_URL = "https://raw.githubusercontent.com/Maulik1430/Hang-man-game-application-API-based-/main"
MAX_WRONG = 6

def get_image_url(wrong_count):
    return f"{BASE_IMG_URL}/hangman_{wrong_count}.png"
    
def word_lookup(length):
    """Fetch a random word of specified length from RapidAPI."""
    url = f"https://random-word-api.p.rapidapi.com/LS/{length}/1"  
    
    headers = {
        "Content-Type": "application/json",  
        "x-rapidapi-host": "random-word-api.p.rapidapi.com",  
        "x-rapidapi-key": "57a7579205msh50b912bf08c80b6p18afbdjsn6fe74ac1ff13"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)  
        response.raise_for_status()  
        
        data = response.json()
        
        if isinstance(data, list) and len(data) > 0:
            return data[0].upper()
        elif isinstance(data, dict) and 'word' in data:
            return data['word'].upper()
        else:
            print(f"Unexpected API response: {data}")
            return "PYTHON"  
            
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return "PYTHON"  
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "PYTHON"  

def start_game(length):
    st.session_state["word"] = word_lookup(length)
    st.session_state["guessed"] = []
    st.session_state["wrong"] = 0
    st.session_state["game_over"] = False
    st.session_state["started"] = True

def reset_game():
    st.session_state.clear()

def main():
    st.set_page_config(page_title="Hangman 🎯", layout="centered")
    st.title("🎯 Hangman Game")

    if "started" not in st.session_state:
        st.session_state["started"] = False

    # 🎯 SETUP SCREEN
    if not st.session_state["started"]:
        st.subheader("Setup Game")

        length = st.slider("Select Word Length", 3, 10, 5)

        if st.button("▶️ Start Game"):
            start_game(length)
            st.rerun()

        return  # ✅ correctly inside main()

    # 🎮 GAME
    word = st.session_state["word"]

    display = " ".join([
        c if c in st.session_state["guessed"] else "_"
        for c in word
    ])

    st.markdown(f"## {display}")

    st.image(get_image_url(st.session_state["wrong"]), width=250)

    st.write(f"❌ Wrong guesses: {st.session_state['wrong']} / {MAX_WRONG}")

    # Game status
    if st.session_state["wrong"] >= MAX_WRONG:
        st.error(f"💀 You lost! Word was: {word}")
        st.session_state["game_over"] = True

    elif all(c in st.session_state["guessed"] for c in word):
        st.success("🎉 You won!")
        st.session_state["game_over"] = True

    # Letters
    if not st.session_state["game_over"]:
        cols = st.columns(7)
        for i, letter in enumerate(string.ascii_uppercase):
            if letter not in st.session_state["guessed"]:
                if cols[i % 7].button(letter):
                    st.session_state["guessed"].append(letter)
                    if letter not in word:
                        st.session_state["wrong"] += 1
                    st.rerun()
            else:
                cols[i % 7].button(letter, disabled=True)

    # Reset
    if st.button("🔁 New Game"):
        reset_game()
        st.rerun()

if __name__ == "__main__":
    main()
