import random

your_action = input("Either play a rock, paper or scissors. I chose: ")

available_actions = ["rock", "paper", "scissors"]

comp_action = random.choice(available_actions)

print(f"You chose {your_action}, computer chose {comp_action}")
if your_action == comp_action:
    print(f"You chose {your_action} while computer chose {comp_action}, It's a TIE!")
#for a tie sasa
elif your_action == "rock":
    if comp_action == "scissors":
        print("Rock smashes scissors! You WIN!")
else:
    print("Paper covers Rock! You LOSE")
elif your_action == "scissors":
     if comp_action == "paper":
        print("Scissors cuts paper! You WIN!")
else:
      print("Rock smashes Scissors, you LOSE!")
elif your_action == "paper":
if comp_action == "rock":
    print("Paper covers Rock! You WIN!")
else:
    print("Scissors cuts paper! You LOSE!")
