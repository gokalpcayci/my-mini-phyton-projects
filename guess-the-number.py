import random

def guessing_name():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        random_number = random.randint(0, 100)
        print("You have 10 attempts remaining to guess the number.")
        for i, attempt in enumerate(range(0, 10)):
            attempt = int(input("Make a guess: "))
            if i != 9:
                if attempt > random_number:
                    print(f"You have {9 - i} attempts remaining to guess the number.")
                    print("Too high")
                elif random_number > attempt:
                    print(f"You have {9 - i} attempts remaining to guess the number.")
                    print("Too low")
                elif random_number == attempt:
                    print(f"You got it! The answer was {random_number}.")
                    break
            else:
                print("You've run out of guesses, you lose.")

    elif difficulty == "hard":
        random_number = random.randint(0, 100)
        print("You have 5 attempts remaining to guess the number.")
        for i, attempt in enumerate(range(0, 5)):
            attempt = int(input("Make a guess: "))
            if i != 4:
                if attempt > random_number:
                    print(f"You have {4 - i} attempts remaining to guess the number.")
                    print("Too high")
                elif random_number > attempt:
                    print(f"You have {4 - i} attempts remaining to guess the number.")
                    print("Too low")
                elif random_number == attempt:
                    print(f"You got it! The answer was {random_number}.")
                    break
            else:
                print("You've run out of guesses, you lose.")



guessing_name()
