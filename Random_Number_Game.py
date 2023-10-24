import random

def main():
    print("Guess the random number game!")
    rand_number, upper_range = random_number()
    guess, user_guess = random_guess_check(rand_number, upper_range)
    if guess == 1:
        print(f"Well done. It took you 1 guess. \nYou guessed {user_guess} and the answer was {rand_number}.")
    else:
        print(f"Well done. It took you {guess} guesses. \nYou guessed {user_guess} and the answer was {rand_number}.")

def random_number():
    while True:
        upper_range = input("Select a number: ")
        if upper_range.isdigit():
            upper_range = int(upper_range)
            if upper_range < 1:
                print(f"{upper_range} is less than 1. Enter a positive number.")
                continue
            else:
                break
        else:
            print(f"{upper_range} is not a number")
            continue
    return random.randint(1, upper_range), upper_range

def user_number(upper_range):
    while True:
        user_guess = input(f"A random number has been chosen between 1 & {upper_range}. Pick a number you think it is: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess < 1:
                print(f"{user_guess} is less than 1. Enter a positive number.")
                continue
            else:
                break
        else:
            print(f"{user_guess} is not a number.")
            continue
    return user_guess

def random_guess_check(rand_number, upper_range):
    guess = 1
    while True:
        user_guess = user_number(upper_range)
        if rand_number > user_guess:
            print(f"You guessed too low. Try again.")
            guess += 1
            continue
        elif rand_number < user_guess:
            print(f"Your guess is too high. Try again")
            guess += 1
            continue
        else:
            break
    return guess, user_guess

if __name__ == "__main__":
    main()