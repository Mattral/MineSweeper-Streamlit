import streamlit as st
import random
import time
from streamlit.ReportThread import get_report_ctx

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
    .custom-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Whack-a-Mole Game
st.title("Whack-a-Mole Game")

# Game parameters
grid_size = 4
game_over = False
score = 0
active_mole = None
duration = 0.5  # Duration for mole appearance

# Create a grid
grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]

# Function to update the game
def update_game():
    global active_mole, score
    active_mole = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    score = 0

# Start a new game
update_game()

st.text("Click on the moles as quickly as possible!")

if st.button("Start Game"):
    update_game()

# Create a custom grid for the game
st.markdown("<div class='custom-grid'>", unsafe_allow_html=True)
for row in range(grid_size):
    for col in range(grid_size):
        # Handle the active mole
        if game_over and (row, col) == active_mole:
            st.button(f"Mole\nScore: {score}", key=(row, col))
        elif st.button("", key=(row, col)):
            if (row, col) == active_mole:
                score += 1
            update_game()

st.markdown("</div>", unsafe_allow_html=True)

# Game over condition
if score >= 10:
    st.text("Congratulations! You win!")
elif game_over:
    st.text("Game Over. Try again!")

st.text("Pro Tip: You can enhance this game with animations and sound effects for a better experience.")
