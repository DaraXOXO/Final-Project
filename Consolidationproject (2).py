import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)


def play_turn(player_name):
    print(f"{player_name}'s turn:")
    dice = roll_dice()
    print(f"Rolled: {dice}")

    if len(set(dice)) == 1:
        print("Tupled out! Score for this turn: 0")
        return 0
    
    fixed_dice = [die for die in dice if dice.count(die) > 1]
    score = sum(fixed_dice)

    while True:
        roll_again = input(f"Current score: {score}. Roll again? (y/n) ")
        if roll_again.lower() == "n":
            break
        new_rolls = []
        for die in dice:
            if die not in fixed_dice:
                new_rolls.append(random.randint(1, 6))
            else:
                new_rolls.append(die)

        dice = tuple(new_rolls)
        print(f"Rolled: {dice}")

    if len(set(dice)) == 1:
        print("Tupled out! Score for this turn: 0")
        return 0
    
    fixed_dice = [die for die in dice if dice.count(die) > 1]
    score = sum(fixed_dice)
    print(f"Final score for this turn: {score}")
    return score
def main():
    """
    Main function to run the game.
    """
    # Get player names from the user
    player_names = input("Enter player names (separated by commas): ").split(",")
    scores = {name: 0 for name in player_names}  # Initialize scores for each player
    winning_score = 50  # Set the winning score
    max_turns = 5  # Set the maximum number of turns

    for turn in range(max_turns):
        print(f"\nTurn {turn + 1}:")  # Print the current turn number
        for player in player_names:
            scores[player] += play_turn(player)  # Play a turn for the player and update their score
            print(f"Current scores: {scores}")  # Print the current scores

            # Check if any player has reached the winning score
            if max(scores.values()) >= winning_score:
                winners = [name for name, score in scores.items() if score >= winning_score]
                print(f"Game over! Winners: {', '.join(winners)}")
                return  # Exit the game if there is a winner

    # If no player reached the winning score, determine the winner(s) based on the highest score(s)
    winners = [name for name, score in scores.items() if score == max(scores.values())]
    print(f"Game over! Winners: {', '.join(winners)}")

if __name__ == "__main__":
    main()
    