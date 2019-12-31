import random

turn = True

print("this is rock paper scissors game!")
p_name = input("Enter your Name: ")
a = ["rock", "paper", "scissors"]

for i in range(2):
    if turn == True:
        player = input("Enter your Choice(rock, paper, scissors): ")

        turn = False
    elif turn == False:
        computer = random.choice(a)
        print("computers choice :", computer)

        turn = True


def win():
    if player == "rock" and computer == "scissors":
        print(p_name, "win Rock blunts scissors")
    elif player == "paper" and computer == "rock":
        print(p_name, "win Rock blunts scissors")
    elif player == "scissors" and computer == "paper":
        print(p_name, "win Rock blunts scissors")
    elif computer == "rock" and player == "scissors":
        print("computer win Rock blunts scissors")
    elif computer == "paper" and player == "rock":
        print("computer win Rock blunts scissors")
    elif computer == "scissors" and player == "paper":
        print("computer win Rock blunts scissors")
    elif player == "rock" and computer == "rock" or \
            player == "paper" and computer == "paper" or \
            player == "scissors" and computer == "scissors":
        print("its a tie!")


win()
