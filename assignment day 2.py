import random

def check_bet_results(bet, scenario):
    if bet == scenario:
        return "YOU WIN!"
    elif any(b == s for b, s in zip(bet, scenario)):
        return "partially win!"
    else:
        return "YOU LOSE!"

def generate_scenario():
    return [random.randint(1, 3) for _ in range(3)]

def play_game():
    print("Welcome to the Betting Game!")
    
    while True:
        start = input("Press 's' to start the game or 'q' to quit: ").lower()
        if start == 'q':
            print("Thanks for playing! Goodbye.")
            break
        elif start == 's':
            bet = [int(input(f"Enter your bet for position {i+1} (1-3): ")) for i in range(3)]
            scenario = generate_scenario()
            result = check_bet_results(bet, scenario)
            
            print(f"\nYour bet: {bet}")
            print(f"Scenario: {scenario}")
            print(result)
        else:
            print("Invalid input. Please press 's' to start or 'q' to quit.")
play_game()
