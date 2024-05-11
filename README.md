# Final-Project
# README.md

# Word Guessing Game

This is a simple word guessing game implemented in Python. The game supports multiple players taking turns to guess a randomly selected secret word from a word bank.

## How to Play

1. Run the `word_guessing_game.py` script to start the game.
2. The game will prompt the current player to enter a letter guess or the word.
3. If the guessed letter is present in the secret word, the game will update the partially revealed word.
4. If the guessed word is correct, the player's score will be updated based on the number of letter guesses made.
5. Players have a limited number of word guesses (3 by default).
6. The game continues until all players have either guessed the word or run out of word guesses.
7. The final scores for all players will be displayed at the end of the game.

## Features

- Multiplayer support
- Randomly selected secret word
- Scoring based on the number of letter guesses
- Limited word guesses per player
- Optional file I/O for loading word bank and saving high scores

## Limitations

- The game does not currently support adding new words to the word bank during runtime.
- There is no persistent storage for high scores across multiple game sessions.

## How to Run

To run the game, simply execute the `word_guessing_game.py` script:
