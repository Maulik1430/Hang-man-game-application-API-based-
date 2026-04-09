import streamlit as st
import requests

BASE_IMG_URL = "https://github.com/Maulik1430/Hang-man-game-application-API-based-/tree/main"

def get_image_url(wrong_count):
    return f"{BASE_IMG_URL}/hangman_{wrong_count}.png"


def word_lookup(word_length):
    url = "https://random-word-api.vercel.app/api?words=1&type=uppercase&length=" + str(word_length)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return "ERROR"


def main():
    st.title("Hangman Game")

    word_length = st.slider("Select word length:", 3, 9, 5)

    if 'word' not in st.session_state:
        st.session_state['word'] = word_lookup(word_length)
        st.session_state['wrong_count'] = 0
        st.session_state['correct_letters'] = []

    word = st.session_state['word']

    letter = st.text_input("Enter a letter:", max_chars=1).upper()

    if st.button("Reset Game"):
        st.session_state.clear()
        st.rerun()

    # Only process when user enters something
    if letter:
        if letter not in word:
            st.session_state['wrong_count'] += 1
        else:
            if letter not in st.session_state['correct_letters']:
                st.session_state['correct_letters'].append(letter)

    # Build display word
    display_word = " ".join([
        char if char in st.session_state['correct_letters'] else "_"
        for char in word
    ])

    col1, col2 = st.columns(2)

    with col1:
        st.code(display_word)

    with col2:
        img_url = get_image_url(st.session_state['wrong_count'])
        st.image(img_url)

    st.write(f"Wrong guesses: {st.session_state['wrong_count']}")

    if st.session_state['wrong_count'] >= 7:
        st.error(f"You lost! Word was: {word}")

    if word == display_word.replace(" ", ""):
        st.success("🎉 You guessed it!")

if __name__ == "__main__":
    main()
