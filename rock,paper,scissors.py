#ROCK,PAPER,SCISSORS..PROJECT IN PYTHON
import random

choice = ["rock", "paper", "scissors",]

while True:
    user = input("Choice rock,paper,scissors or exit:").lower()

    if user == "exit":
        print("Game over!")
        break
    if user not in choice:
        print("Invalid choice!")
        continue
    computer = random.choice(choice)
    print("Youe:",user)
    print("Computer:", computer)


    cmputer= random.choice(choice)

    print("You:",user)
    print("Computer:",computer)

    computer = random.choice(choice)
    print("You:", user)
    print("Computer:", computer)

computer == random.choice(choice)
print("You:", user)
print("Computer:",computer)
if user == computer:
    print("It's a tie!")
elif user =="rock" and computer=="scissors":
    print("You win!")
elif user =="paper" and computer=="rock":
    print("You win!")
elif user =="scissor" and computer =="paper":
    print("You win!")
else:
    print("Computer wins!")                