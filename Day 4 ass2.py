import random  # Import the random module to generate random numbers

# Function to check bet results
def check_bet_results(bet, scenario):
    if bet == scenario:  # Check if the bet exactly matches the scenario
        return "YOU WIN!"  # Return "YOU WIN!" if there's an exact match
    elif any(b == s for b, s in zip(bet, scenario)):  # Check if any element in the bet matches the scenario
        return "partially win!"  # Return "partially win!" if there's a partial match
    else:
        return "YOU LOSE!"  # Return "YOU LOSE!" if there's no match

# Function to generate a random scenario
def generate_scenario():
    return [random.randint(1, 3) for _ in range(3)]  # Generate a list of three random numbers between 1 and 3

# Function to play the game
def play_game():
    print("Welcome to the Betting Game!")  # Print a welcome message
    
    while True:  # Start an infinite loop to keep the game running
        start = input("Press 's' to start the game or 'q' to quit: ").lower()  # Prompt the user to start or quit
        if start == 'q':  # If the user chooses to quit
            print("Thanks for playing! Goodbye.")  # Print a goodbye message
            break  # Break the loop to end the game
        elif start == 's':  # If the user chooses to start the game
            # Collect bets from the player
            bet = [int(input(f"Enter your bet for position {i+1} (1-3): ")) for i in range(3)]  # Prompt the user for their bet
            scenario = generate_scenario()  # Generate a random scenario
            result = check_bet_results(bet, scenario)  # Check the result of the bet
            
            # Display results
            print(f"\nYour bet: {bet}")  # Print the player's bet
            print(f"Scenario: {scenario}")  # Print the generated scenario
            print(result)  # Print the result of the bet
        else:  # If the user input is invalid
            print("Invalid input. Please press 's' to start or 'q' to quit.")  # Print an error message

# Run the game
play_game()  # Call the play_game function to start the game
