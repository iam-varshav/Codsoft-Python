import random
options = ("rock","paper","scissors")
player=None
computer=random.choice(options)

while player not in options:
    player = input("Enter a choice: ")
print(f"Player: {player}")
print(f"Computer: {computer}")

if player== computer:
    print("Its is a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
else:
    print("You lose!")
