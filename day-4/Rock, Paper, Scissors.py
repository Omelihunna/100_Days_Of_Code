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

# Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(f"User chose:\n{rock}")
elif user_choice == 1:
    print(f"User chose:\n{paper}")
else:
    print(f"User chose:\n{scissors}")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"computer chose:\n{rock}")
elif computer_choice == 1:
    print(f"computer chose:\n{paper}")
else:
    print(f"computer chose:\n{scissors}")

if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (
        user_choice == 2 and computer_choice == 0):
    print("You lose")
elif user_choice == computer_choice:
    print("It's a draw")
else:
    print("You Win")