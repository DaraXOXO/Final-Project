import random

# Define the word bank
word_bank = ['python', 'javascript', 'ruby', 'java', 'csharp']

# Function to randomly select a secret word
def select_secret_word():
    return random.choice(word_bank)

# Initialize player data
players = [
    {'name': 'Player 1', 'score': 0, 'letter_guesses': 0, 'word_guesses': 3},
    {'name': 'Player 2', 'score': 0, 'letter_guesses': 0, 'word_guesses': 3}
]
current_player_index = 0
secret_word = select_secret_word()

def play_game():
    global current_player_index, secret_word

    while True:
        player = players[current_player_index]
        partially_revealed_word = ['_'] * len(secret_word)

        while player['word_guesses'] > 0:
            print(f"\nCurrent word: {''.join(partially_revealed_word)}")
            print(f"{player['name']}, guess a letter or the word (remaining word guesses: {player['word_guesses']}):")
            guess = input().lower()

            if len(guess) == 1:  # Letter guess
                if guess in secret_word:
                    for i in range(len(secret_word)):
                        if secret_word[i] == guess:
                            partially_revealed_word[i] = guess
                else:
                    player['letter_guesses'] += 1

            else:  # Word guess
                if guess == secret_word:
                    player['score'] = player['letter_guesses']
                    print(f"{player['name']} guessed the word correctly!")
                    break
                else:
                    player['word_guesses'] -= 1
                    print("Incorrect word guess.")

            if '_' not in partially_revealed_word:
                player['score'] = player['letter_guesses']
                print(f"{player['name']} guessed the word correctly!")
                break

        if player['word_guesses'] == 0:
            print(f"{player['name']} ran out of word guesses. The word was: {secret_word}")

        current_player_index = (current_player_index + 1) % len(players)
        if current_player_index == 0:
            break

    print("\nGame over! Final scores:")
    for player in players:
        print(f"{player['name']}: {player['score']}")

 # Display game state

    print(f"\nCurrent word: {''.join(partially_revealed_word)}")
    print(f"{player['name']}, guess a letter or the word (remaining word guesses: {player['word_guesses']}):")

# Get user input

guess = input().lower()

# Provide feedback
if is_word_guess_correct(guess, secret_word):
     print(f"{player['name']} guessed the word correctly!")
else:
     print("Incorrect word guess.")

# Load word bank from file
with open('word_bank.txt', 'r') as file:
    word_bank = [line.strip() for line in file.readlines()]

# Save high scores to file
with open('high_scores.txt', 'w') as file:
    for player in players:
        file.write(f"{player['name']}: {player['score']}\n")
