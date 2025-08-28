import random  # To let the computer choose randomly

print('Snake-Water-Gun')  # Title of the game

# Ask the user how many rounds to play
try:
    n = int(input('Enter number of rounds: '))  # Convert input to integer
except (ValueError, EOFError):  # Handle invalid input or unexpected EOF
    print("Invalid input or EOF detected. Exiting the game.")
    exit()  # Stop the program safely

# Possible choices
options = ['s', 'w', 'g']

# Variables to keep track of scores and rounds
rounds = 1
comp_win = 0
user_win = 0

# Function to decide who wins a round
def round_winner(player, computer):
    # If both choices are the same → it's a draw
    if player == computer:
        return "draw"
    # Winning conditions for the player
    elif (player == 's' and computer == 'w') or \
         (player == 'w' and computer == 'g') or \
         (player == 'g' and computer == 's'):
        return "user"  # Player wins
    else:
        return "computer"  # Otherwise, computer wins

# Loop through all rounds
while rounds <= n:
    # Show current round and options
    print(f"\nRound {rounds}")
    print("Snake - 's'\nWater - 'w'\nGun - 'g'")

    # Get player's choice
    try:
        player = input('Choose your option: ').lower()  # Convert to lowercase
    except EOFError:  # If input suddenly ends
        print("\nEOF detected. Ending the game early.")
        break  # Exit the loop

    # Check for invalid input
    if player not in options:
        print('Invalid input, try again.')
        continue  # Restart the current round without increasing counter

    # Let the computer randomly choose
    computer = random.choice(options)

    # Decide who won the round
    winner = round_winner(player, computer)

    # Update scores and show result of the round
    if winner == "user":
        user_win += 1
        print(f"You chose {player}, computer chose {computer}. You won this round!")
    elif winner == "computer":
        comp_win += 1
        print(f"You chose {player}, computer chose {computer}. Computer won this round!")
    else:
        print(f"You chose {player}, computer chose {computer}. This round is a draw!")

    # Go to the next round
    rounds += 1

# After all rounds, show the final result
print("\n--- Final Result ---")
if user_win > comp_win:
    print(f"🎉 Congratulations! You won the game ({user_win} - {comp_win})")
elif comp_win > user_win:
    print(f"💻 Computer won the game ({comp_win} - {user_win})")
else:
    print(f"🤝 The game is a draw ({user_win} - {comp_win})")
