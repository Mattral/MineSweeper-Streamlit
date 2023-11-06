import streamlit as st
import random

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

st.title("Minesweeper Game")

size = st.slider("Select the size of the Minesweeper grid:", 5, 20, 10)

# Generate the Minesweeper grid
grid = [[0 for _ in range(size)] for _ in range(size)]
mines = random.sample(range(size * size), size)

for mine in mines:
    row, col = divmod(mine, size)
    grid[row][col] = "X"

# Define directions for adjacent cells
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def count_adjacent_mines(row, col):
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < size and 0 <= c < size and grid[r][c] == "X":
            count += 1
    return count

def reveal(row, col):
    if 0 <= row < size and 0 <= col < size:
        if grid[row][col] == 0:
            grid[row][col] = count_adjacent_mines(row, col)
            if grid[row][col] == 0:
                for dr, dc in directions:
                    reveal(row + dr, col + dc)

for row in range(size):
    for col in range(size):
        if st.button("", key=f"{row}-{col}", args=(row, col)):
            if grid[row][col] == "X":
                st.markdown("You hit a mine! Game over.")
            else:
                reveal(row, col)

st.text("Left-click to reveal a tile.")
st.text("Right-click to flag a potential mine.")
