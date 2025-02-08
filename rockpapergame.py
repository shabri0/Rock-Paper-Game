import random

# Display game instructions
print("Welcome to Rock, Paper, Scissors!")

# Get the user's choice
print("Enter your choice: rock, paper, or scissors")
user_choice = input().lower()

# Ensure the user enters a valid choice
while user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
    user_choice = input().lower()

# Get the computer's choice
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Display the choices
print(f"\nYou chose: {user_choice}")
print(f"The computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'scissors' and computer_choice == 'paper') or \
     (user_choice == 'paper' and computer_choice == 'rock'):
    print("You win!")
else:
    print("You lose!")
