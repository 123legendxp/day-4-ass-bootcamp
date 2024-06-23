import random

def player_turn():
    # Get player's choice
    return input("Choose 'fold' or 'unfold': ").strip().lower()

def computer_turn():
    # Randomly choose 'fold' or 'unfold' for the computer
    choice = random.choice(['fold', 'unfold'])
    print(f"Computer chose: {choice}")
    return choice

def determine_winner(player_choice, computer_choice):
    # Determine the winner or if it's a draw
    if player_choice == computer_choice:
        return "draw"
    return random.choice(['player', 'computer'])

def game(rounds):
    # Play the specified number of rounds
    for _ in range(rounds):
        player_choice = player_turn()
        if player_choice not in ['fold', 'unfold']:
            print("Invalid choice.")
            continue
        computer_choice = computer_turn()
        winner = determine_winner(player_choice, computer_choice)
        print(f"Winner: {winner}")

if __name__ == "__main__":
    # Get the number of rounds from the user and start the game
    rounds = int(input("Enter number of rounds: "))
    game(rounds)
