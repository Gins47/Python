import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x} "))
        if guess > random_number:
            print(f"The random number is low")
        elif guess < random_number:
            print(f"The random number is high")

    print(f"Wow, Congratulation your guess is right")


guess(10)
