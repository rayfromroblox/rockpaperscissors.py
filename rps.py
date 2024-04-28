import random

choices = ("rock", "paper", "scissors")

playing = True
while playing:
    player_choice = None
    computer_choice = random.choice(choices)

    while player_choice not in choices:
        player_choice = input("Enter a choice, either rock, paper, or scissors:")

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("it's a Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n):").lower()
    if not play_again == "y":
        playing = False

print("Thanks for playing!")
