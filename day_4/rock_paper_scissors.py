import random
import art

choice_names = ['rock', 'paper', 'scissors']


# Write your code below this line 👇
def print_choices():
    print(f"human choice {choice_names[human_choice]}\n{art.choices_array[human_choice]}")
    print(f"computer choice {choice_names[computer_choice]}\n{art.choices_array[computer_choice]}")


human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

choices = [0, 1, 2]
computer_choice = random.choice(choices)
# could also use random.randint(0,2) in python

if human_choice == computer_choice:
    print("Draw")
    print_choices()
elif human_choice == 0 and computer_choice == 1 or human_choice == 1 and computer_choice == 2 or human_choice == 2 and computer_choice == 0:
    print("You Lost")
    print_choices()
elif human_choice == 0 and computer_choice == 2 or human_choice == 2 and computer_choice == 1 or human_choice == 1 and computer_choice == 0:
    print("You won!")
    print_choices()
else:
    print_choices()

