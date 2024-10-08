import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Function to display the result
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Type 'exit' to quit the game.")

        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print(f"\nFinal Score: You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        rounds += 1
        print(f"\nCurrent Score after {rounds} rounds: You: {user_score} | Computer: {computer_score}")

        # Ask the user if they want to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nFinal Score: You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

# Start the game
play_game()
