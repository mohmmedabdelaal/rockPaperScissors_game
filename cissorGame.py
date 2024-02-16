import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

CHOICES = [rock, paper, scissors]


def get_user_choice():
    while True:
        try:
            choice = input("choose 0 for Rock, 1 for Paper nad 2 for Scissors, or type 'exit' to end: ")
            if choice.lower() == 'exit':
                return None
            else:
                choice = int(choice)
                if 0 <= choice <= 2:
                    return choice
                else:
                    print("Invalid input. Please Enter 0, 1, 2 or 'exit' to end.")
        except ValueError:
            print("Invalid input. Please Enter a number or 'exit'.")


def determine_winner(user_choice, computer_choice):
    if user_choice is None:
        return "Game ended."
    elif user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        return "Congratulations you win!"
    else:
        return "You lose!"


def print_choices():
    print("0: Rock\n1: Paper\n2:Scissors")


def main():
    while True:
        print_choices()
        user_choice = get_user_choice()

        if user_choice is None:
            break  # Exit the loop if the user choose to exit

        computer_choice = random.randint(0, 2)

        print("\nYou choice:")
        print(CHOICES[user_choice])

        print("\nComputer's choice:")
        print(CHOICES[computer_choice])

        result = determine_winner(user_choice, computer_choice)
        print(result)


if __name__ == "__main__":
    main()
