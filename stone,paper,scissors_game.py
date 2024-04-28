import random

while True:

    choices=['stone','paper','scissors']
    computer= random.choice(choices)
    player= None
    while player not in choices:
        player=input("stone, paper or scissors?").lower()
    if player==computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("It's a Tie!")
    elif player=="stone":
        if computer=="paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")
        if computer=="scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
    elif player=="paper":
        if computer=="scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")
        if computer=="stone":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
    elif player=="scissors":
        if computer=="stone":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")
        if computer=="paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
    play_again= input("Do you wanna play again?(yes/no)").lower()
    if play_again!="yes":
        break
print("Good Game!")