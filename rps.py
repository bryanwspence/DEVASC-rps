# Welcome message
print("Welcome to Rock/Paper/Scissors")

rps = ["rock", "paper", "scissors"]

while True:
    # Get Player 1's choice
    player1 = input("\nPlayer 1 - Please enter Rock, Paper, or Scissors: ")

    if player1.lower() not in rps:
        print("\nPlease enter Rock, Paper, or Scissors")
        continue
    # Get Player 2's choice
    player2 = input("\nPlayer 2 - Please enter Rock, Paper, or Scissors: ")

    if player2.lower() not in rps:
        print("\nPlease enter Rock, Paper, or Scissors")
        continue

    if player1.lower() == "rock" and player2.lower() == "paper":
        print("\nPlayer 2 wins!")

    elif player1.lower() == "rock" and player2.lower() == "scissors":
        print("\nPlayer 1 wins!")

    elif player1.lower() == "paper" and player2.lower() == "rock":
        print("\nPlayer 1 wins!")

    elif player1.lower() == "paper" and player2.lower() == "scissors":
        print("\nPlayer 2 wins!")

    elif player1.lower() == "scissors" and player2.lower() == "rock":
        print("\nPlayer 2 wins!")

    elif player1.lower() == "scissors" and player2.lower() == "paper":
        print("\nPlayer 1 wins!")

    else:
        print("\nDraw!")

    quit = input("\nWould you like to play again? ")

    if quit.lower() == "yes":
        continue
    else:
        exit()


