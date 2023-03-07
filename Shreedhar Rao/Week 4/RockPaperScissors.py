# Rock-Paper-Scissors game with computer
import random
user = input("Enter 'r' for Rock 'p' for Paper or 's' for Scissors: ")

computer = random.choice(['r','p','s'])

# Rock beats Scissor
# Paper beats Rock
# Scissor beats Paper

if user == 'r' and computer == 's':
    print("Computer selected Scissors and you won!")
elif user == 'p' and computer == 'r':
    print("Computer selected Rock and you won!")
elif user == 's' and computer == 'p':
    print("Computer selected Paper and you won!")
elif user == 'p' and computer == 's':
    print(f"Computer selected Scissors and you lost!")
elif user == 'r' and computer == 'p':
    print(f"Computer selected Paper and you lost!")
elif user == 's' and computer == 'r':
    print(f"Computer selected Rock and you lost!")

if user == computer:
    print(f"Computer selected the same thing and it was a tie!")