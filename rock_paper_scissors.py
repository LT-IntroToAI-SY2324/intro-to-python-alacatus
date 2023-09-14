import random
choices = ["rock","paper","scissors"]

player = input("Enter a choice (rock, paper, scissors): ")
bot = random.choice(choices)

print(f"you chose {player}, computer chose {bot}")

if player == bot:
    print("both chose the same, you tie!")
elif player == "scissors" and bot == "rock":
    print("rock smashes scissors, you lose!")
elif player == "rock" and bot == "scissors":
    print("rock smashes scissors, you win!")
elif player == "scissors" and bot == "paper":
    print("scissors cut paper, you win!")
elif player == "paper" and bot == "scissors":
    print("scissors cut paper, you lose!")
elif player == "paper" and bot == "rock":
    print("paper smothers rock, you win!")
elif player == "rock" and bot == "paper":
    print("paper smothers rock, you lose!")
