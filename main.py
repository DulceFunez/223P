import streamlit as st
import random

# List of possible words for Hangman
word_list = ["python", "streamlit", "hangman", "developer", "machinelearning", "artificialintelligence"]

# Function to start or reset the game
def start_game():
    # Title and instructions
    st.title("Hangman Game")
    st.write("Guess the word by entering letters. You have 8 attempts.")
    
    # Display the author's name in smaller letters
    st.markdown("<h5 style='text-align: center;'>by Dulce Funez</h5>", unsafe_allow_html=True)

    # Initialize session state variables if they don't exist
    if "word_to_guess" not in st.session_state:
        st.session_state.word_to_guess = random.choice(word_list).lower()
    if "guessed_letters" not in st.session_state:
        st.session_state.guessed_letters = []
    if "remaining_attempts" not in st.session_state:
        st.session_state.remaining_attempts = 8
    if "correct_guesses" not in st.session_state:
        st.session_state.correct_guesses = ["_"] * len(st.session_state.word_to_guess)

    # Show the word with guessed letters and underscores
    display_word = " ".join(st.session_state.correct_guesses)
    st.write(f"Word to Guess: {display_word}")
    
    # Display remaining attempts
    st.write(f"Remaining Attempts: {st.session_state.remaining_attempts}")
    
    # If attempts are 0, end the game
    if st.session_state.remaining_attempts == 0:
        st.write("Game Over! You've run out of attempts.")
        st.write(f"The word was: {st.session_state.word_to_guess}")
        if st.button("Play Again"):
            reset_game()
        return  # Stop further execution

    # Input field for user's guess, only if attempts are available
    guess = st.text_input("Enter a letter:", max_chars=1).lower()
    
    # Button to submit guess, only if attempts are available
    if st.button("Submit Guess"):

        if guess in st.session_state.guessed_letters:
            st.write("You already guessed this letter! Try another one.")
        elif guess.isalpha() and len(guess) == 1:
            st.session_state.guessed_letters.append(guess)
            if guess in st.session_state.word_to_guess:
                st.write(f"Good job! The letter {guess} is in the word.")
                # Update the correct guesses
                for i in range(len(st.session_state.word_to_guess)):
                    if st.session_state.word_to_guess[i] == guess:
                        st.session_state.correct_guesses[i] = guess
            else:
                st.write(f"Oops! The letter {guess} is not in the word.")
                st.session_state.remaining_attempts -= 1
        else:
            st.write("Please enter a valid letter.")
        
        # Check if the player has guessed the word
        if "_" not in st.session_state.correct_guesses:
            st.write("Congratulations! You've guessed the word!")
            st.write(f"The word was: {st.session_state.word_to_guess}")
            if st.button("Play Again"):
                reset_game()

    # Display previously guessed letters
    if st.session_state.guessed_letters:
        st.write("Previously guessed letters: ", ", ".join(st.session_state.guessed_letters))

# Function to reset the game for a new round with a new word
def reset_game():
    # Choose a new word
    st.session_state.word_to_guess = random.choice(word_list).lower()
    st.session_state.guessed_letters = []  # Clear guessed letters
    st.session_state.remaining_attempts = 8  # Reset attempts
    st.session_state.correct_guesses = ["_"] * len(st.session_state.word_to_guess)  # Reset word display

# Main logic to show the first page with Start button
if "game_started" not in st.session_state or not st.session_state.game_started:
    # First page with welcome message and Start Game button
    st.title("Hangman Game")
    st.write("Welcome to Hangman! Ready to play?")
    st.markdown("<h5 style='text-align: center;'>by Dulce Funez</h5>", unsafe_allow_html=True)
    
    # When the button is clicked, set the game_started flag to True
    if st.button("Start Game"):
        st.session_state.game_started = True
        start_game()

else:
    # The game starts after the user clicks the "Start Game" button
    start_game()
