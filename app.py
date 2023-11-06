import streamlit as st
import random

# Define a list of card pairs (should have at least 2 of each to form pairs)
card_pairs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Shuffle the card pairs randomly
random.shuffle(card_pairs)
cards = card_pairs + card_pairs  # Create pairs

st.title("Memory Card Game")

# Create a 4x4 grid to display the cards
columns = st.beta_columns(4)
selected_cards = []
solved_pairs = 0

for i in range(4):
    for j in range(4):
        idx = i * 4 + j
        if not columns[j].button(f"Card {idx + 1}"):
            continue

        if idx not in selected_cards:
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

st.write("To play, click on the buttons to reveal the cards. Try to find all the matching pairs.")
