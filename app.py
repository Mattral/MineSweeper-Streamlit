import streamlit as st
import random

# Define a list of card pairs (should have at least 2 of each to form pairs)
card_pairs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Shuffle the card pairs randomly
random.shuffle(card_pairs)
cards = card_pairs + card_pairs  # Create pairs

st.title("Memory Card Game")

# Add some custom CSS to style the grid
st.markdown(
    """
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }
    .grid-item {
        background-color: #e0e0e0;
        padding: 20px;
        text-align: center;
        font-size: 24px;
    }
    </style>
    """
)

selected_cards = []
solved_pairs = 0

# Create a grid container
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

for idx in range(16):
    if idx in selected_cards:
        continue

    if st.button(f'<div class="grid-item">Card {idx + 1}</div>', key=idx):
        selected_cards.append(idx)

        if len(selected_cards) == 2:
            if cards[selected_cards[0]] == cards[selected_cards[1]]:
                solved_pairs += 1
                st.success("You found a pair!")
            else:
                st.warning("Not a match. Try again!")

            # Clear selected cards
            selected_cards = []

    if solved_pairs == len(card_pairs):
        st.success("Congratulations! You've matched all the pairs!")

# Close the grid container
st.markdown('</div>', unsafe_allow_html=True)

st.write("To play, click on the buttons to reveal the cards. Try to find all the matching pairs.")
