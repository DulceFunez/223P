import streamlit as st
import random

word_list = ["elephant", "mansion", "honduras", "chicago"]

def reset_game():
    st.session_state.word_to_guess = random.choice(word_list).lower()
    st.session_state.guessed_letters = [] 
    st.session_state.remaining_attempts = 8
    st.session_state.correct_guesses = ["_"] * len(st.session_state.word_to_guess)

def start_game():

    st.title("Hangman Game")
    st.write("Guess the word by entering letters. You have 8 attempts.")

    if "word_to_guess" not in st.session_state:
        st.session_state.word_to_guess = random.choice(word_list).lower()
    if "guessed_letters" not in st.session_state:
        st.session_state.guessed_letters = []
    if "remaining_attempts" not in st.session_state:
        st.session_state.remaining_attempts = 8
    if "correct_guesses" not in st.session_state:
        st.session_state.correct_guesses = ["_"] * len(st.session_state.word_to_guess)

    display_word = " ".join(st.session_state.correct_guesses)
    st.write(f"Word to Guess: {display_word}")
    
    st.write(f"Remaining Attempts: {st.session_state.remaining_attempts}")
    
    if st.session_state.remaining_attempts == 0:
        st.write("Game Over! You've run out of attempts.")
        st.write(f"The word was: {st.session_state.word_to_guess}")
        if st.button("Play Again"):
            reset_game()
        return

    guess = st.text_input("Enter a letter:", max_chars=1).lower()
    
    if st.button("Submit Guess"):

        if guess in st.session_state.guessed_letters:
            st.write("You already guessed this letter! Try another one.")
        elif guess.isalpha() and len(guess) == 1:
            st.session_state.guessed_letters.append(guess)
            if guess in st.session_state.word_to_guess:
                st.write(f"Good job! The letter {guess} is in the word.")
                for i in range(len(st.session_state.word_to_guess)):
                    if st.session_state.word_to_guess[i] == guess:
                        st.session_state.correct_guesses[i] = guess
            else:
                st.write(f"Oops! The letter {guess} is not in the word.")
                st.session_state.remaining_attempts -= 1
        else:
            st.write("Please enter a valid letter.")
        
        if "_" not in st.session_state.correct_guesses:
            st.write("Congratulations! You've guessed the word!")
            st.write(f"The word was: {st.session_state.word_to_guess}")
            if st.button("Play Again"):
                reset_game()
            return

    if st.session_state.guessed_letters:
        st.write("Previously guessed letters: ", ", ".join(st.session_state.guessed_letters))

if "game_started" not in st.session_state or not st.session_state.game_started:
    st.title("Hangman Game")
    st.write("by Dulce Funez")
    st.write("Welcome to Hangman! Ready to play?")
    
    if st.button("Start Game"):
        st.session_state.game_started = True
        start_game()

else:
    start_game()
