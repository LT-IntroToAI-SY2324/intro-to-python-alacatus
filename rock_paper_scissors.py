import random
choices = ["rock","paper","scissors"]

player = input("Enter a choice (rock, paper, scissors): ")
bot = random.choice(choices)

print(f"you chose {player}, computer chose {bot}")

if player == bot:
    print("both chose the same, you tie!")
if player == "scissors" and bot == "rock":
    print("rock smashes scissors, you lose!")
if player == "rock" and bot == "scissors":
    print("rock smashes scissors, you win!")
if player == "scissors" and bot == "paper":
    print("scissors cut paper, you win!")
if player == "paper" and bot == "scissors":
    print("scissors cut paper, you lose!")

