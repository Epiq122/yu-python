import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer_choices = [rock, paper, scissors]
random_computer = random.choice(computer_choices)

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
)
if choice == 0:
    print(rock)
    print("Computer Chose: ")
    print(random_computer)
    if random_computer == computer_choices[1]:
        print("You Lose")
    elif random_computer == computer_choices[0]:
        print("Tie")
    else:
        print("You Win")
if choice == 1:
    print(paper)
    print("Computer Chose: ")
    print(random_computer)
    if random_computer == computer_choices[2]:
        print("You Lose")
    elif random_computer == computer_choices[1]:
        print("Tie")
    else:
        print("You Win")
if choice == 2:
    print(scissors)
    print("Computer Chose: ")
    print(random_computer)
    if random_computer == computer_choices[0]:
        print("You Lose")
    elif random_computer == computer_choices[2]:
        print("Tie")
    else:
        print("You Win")
