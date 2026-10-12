import random
number=random.randint(1,200)
print("__number guessing game__")
while True:
    guess=int(input("guess a number(1-200):"))
    if guess==number:
        print("correct you won")
        break
    elif guess<number:
        print("too low")
    else:
        print("too high low")    