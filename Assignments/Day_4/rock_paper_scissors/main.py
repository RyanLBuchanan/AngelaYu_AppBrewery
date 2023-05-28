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

#Write your code below this line 👇
import random

choice_list = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

print(f"My choice:\n\n{choice_list[your_choice]}\n\nComputer chose:\n\n{choice_list[computer_choice]}\n")

if your_choice == computer_choice:
    print("It's a draw!")
elif your_choice == 0 and computer_choice == 1:
    print("You lose!")
elif your_choice == 1 and computer_choice == 2:
    print("You lose!")
elif your_choice == 2 and computer_choice == 0:
    print("You lose!")
else:
    print("You win!!!")




