import streamlit as st
import random
import time

# Set a dark theme for the Streamlit app
st.markdown(
    """
    <style>
    .stApp {
        background: #121212;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background: #121212;
        color: #ffffff;
    }
    .stTextInput > div > label {
        color: #ffffff;
    }
    .stButton > button {
        background: #009688;
        color: #ffffff;
    }
    .stButton > button:hover {
        background: #007a6b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Whack-a-Mole Game")

grid_size = 4
mole_position = (0, 0)
score = 0
game_over = False

def update_game():
    global mole_position, score, game_over
    mole_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    score = 0
    game_over = False

st.text("Click on the moles as quickly as possible!")

grid_container = st.container()
game_container = st.container()

if st.button("Start Game"):
    update_game()

with grid_container:
    for row in range(grid_size):
        for col in range(grid_size):
            if game_over and (row, col) == mole_position:
                st.button(f"Mole\nScore: {score}", key=(row, col))
            elif st.button("", key=(row, col)):
                if (row, col) == mole_position:
                    score += 1
                update_game()

with game_container:
    if score >= 10:
        st.text("Congratulations! You win!")
    elif game_over:
        st.text("Game Over. Try again!")

st.text("Pro Tip: You can enhance this game with animations and sound effects for a better experience.")
