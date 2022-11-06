import random

number = 0
easy_level = 10
hard_level = 5
chances = 0


def generate_num():
    global number
    number = int(random.randint(1,100))


def guess_num():
    global chances
    chances -= 1
    guess = int(input("Guess the number: \n"))
    return guess


def check_guess(guess):
    if guess == number:
        print_results("won")
    elif guess < number:
        print_results("low")
    elif guess > number:
        print_results("high")


def print_results(status):

    if status == "won":
        print(f"You got it!! The answer was {number}")
        replay()
        return
    elif status == "low":
        if not chances == 0:
            print("That's too low! Try again...")
    elif status == "high":
        if not chances == 0:
            print("That's too high! Try again...")
    if chances == 0:
        print(f"Game Over! You ran out of lives. The number was {number}")
        replay()
        return

    print(f"Good Choice! You have {chances} chances to get the number")
    check_guess(guess_num())


def replay():
    play_again = input("Do you want to go again? y/n")
    if play_again == "y":
        start()
    else:
        print("Loser!")


def start():
    global chances
    print("I am thinking of a number between 1 and 100")
    level = int(input("Pick a Level: Type 1 for 'Easy' or 2 for 'Hard':\n"))
    if level == 1:
        chances = 10
        print(f"Good Choice! You have {chances} chances to get the number")
    else:
        chances = 5
        print(f"Good Choice! You have {chances} chances to get the number")
    generate_num()
    check_guess(guess_num())


start()
