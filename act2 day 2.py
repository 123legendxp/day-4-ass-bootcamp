import random

def player_turn():
    return input("Choose 'fold' or 'unfold': ").strip().lower()

def computer_turn():
    choice = random.choice(['fold', 'unfold'])
    print(f"Computer chose: {choice}")
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    return random.choice(['player', 'computer'])

def game(rounds):
    for _ in range(rounds):
        player_choice = player_turn()
        if player_choice not in ['fold', 'unfold']:
            print("Invalid choice.")
            continue
        computer_choice = computer_turn()
        winner = determine_winner(player_choice, computer_choice)
        print(f"Winner: {winner}")

if __name__ == "__main__":
    rounds = int(input("Enter number of rounds: "))
    game(rounds)
