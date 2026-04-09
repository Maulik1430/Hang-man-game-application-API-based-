import streamlit as st
import requests
import string
import random

BASE_IMG_URL = "https://raw.githubusercontent.com/Maulik1430/Hang-man-game-application-API-based-/main"
MAX_WRONG = 6

def get_image_url(wrong_count):
    return f"{BASE_IMG_URL}/hangman_{wrong_count}.png"

def word_lookup(length):
    url = f"https://random-word-api.vercel.app/api?words=5&type=uppercase&length={length}"
    res = requests.get(url)
    if res.status_code == 200:
        return random.choice(res.json())
    return "ERROR"

def init_game(length):
    st.session_state["word"] = word_lookup(length)
    st.session_state["guessed"] = []
    st.session_state["wrong"] = 0
    st.session_state["game_over"] = False
    st.session_state["length"] = length

def main():
    st.set_page_config(page_title="Hangman 🎯", layout="centered")
    st.title("🎯 Hangman Game")

    length = st.slider("Word Length", 3, 9, 5)

    # ✅ FIX: reinitialize if first run OR length changed
    if "word" not in st.session_state or st.session_state.get("length") != length:
        init_game(length)

    word = st.session_state["word"]

    # 🔤 Display word
    display = " ".join([
        c if c in st.session_state["guessed"] else "_"
        for c in word
    ])
    st.markdown(f"## {display}")

    # 🖼️ Image
    st.image(get_image_url(st.session_state["wrong"]), width=250)

    st.write(f"❌ Wrong guesses: {st.session_state['wrong']} / {MAX_WRONG}")

    # 🏁 Game status
    if st.session_state["wrong"] >= MAX_WRONG:
        st.error(f"💀 You lost! Word was: {word}")
        st.session_state["game_over"] = True

    elif all(c in st.session_state["guessed"] for c in word):
        st.success("🎉 You won!")
        st.session_state["game_over"] = True

    # 🔤 Alphabet buttons
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

    # 🔁 Reset button
    if st.button("🔁 New Game"):
        init_game(length)
        st.rerun()

if __name__ == "__main__":
    main()
