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
    try:
        url = f"https://random-word-api.vercel.app/api?words=50&t={time.time()}"
        res = requests.get(url)
        if res.status_code == 200:
            words = res.json()
            filtered = [w.upper() for w in words if len(w) == length]
            if filtered:
                return random.choice(filtered)
            return random.choice(words).upper()
    except:
        pass
    return "ERROR"

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
