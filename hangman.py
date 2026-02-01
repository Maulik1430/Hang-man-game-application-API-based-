import streamlit as st
import requests

def word_lookup(word_length):
    url = "https://random-word-api.vercel.app/api?words=1&type=uppercase&length=" + str(word_length)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return "ERROR"
    
def main():
    st.title("Hangman Game")

    word_length = st.slider("Select word length:", min_value=3, max_value=9, value=5, step=1)

    if 'word' not in st.session_state or len(st.session_state['word']) == 0:
        word = word_lookup(word_length)
        st.session_state['word'] = word
        st.session_state['wrong_count'] = 0
        st.session_state['correct_letters'] = []
    else:
        word = st.session_state['word']

    # st.write(f"The word to guess is: {word}")

    letter = st.text_input("Enter a letter:", max_chars=1).upper()
    st.button("Reset Game", on_click=lambda: st.session_state.clear())

    if not letter in word:
        st.session_state['wrong_count'] += 1
        if st.session_state['wrong_count'] >= 7:
            st.error(f"You've lost! The word was: {word}")
    else:
        st.session_state['correct_letters'].append(letter)

    # showing underscores for each letter in the word
    display_word = ""
    for char in word:
        if char in st.session_state['correct_letters']:
            display_char = char
        else:
            display_char = "_"
        display_word += display_char + " "

    col1, col2 = st.columns(2)
    with col1:
        word_container = st.empty()
        word_container.code(display_word.strip())
    with col2:
        hangman_image = st.empty()
        hangman_image.image(f"images/hangman_{st.session_state['wrong_count']}.png")
    
    st.error(f"Wrong guesses: {st.session_state['wrong_count']}")

    if word == display_word.replace(" ", ""):
        st.success("Congratulations! You've guessed the word!")

if __name__ == "__main__":
    main()