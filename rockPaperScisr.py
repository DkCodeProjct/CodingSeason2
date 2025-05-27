"""
import random

def validInput():
    while True:
        print("type exit to quit")
        inpt = input("enter choice: ")
        if inpt in ["rock", "paper", "scissors", "exit"]:
            return inpt 
        print('invalid input ')

compChoice = ["rock", "paper", "scissors"]

def rules(user, comp):
    if user == comp:
        print("It's a tie!")

    elif user == "rock" and comp == "scissors":
        print("User wins! Rock crushes scissors.")
    elif user == "rock" and comp == "paper":
        print("Computer wins! Paper covers rock.")

    elif user == "paper" and comp == "rock":
        print("User wins! Paper covers rock.")
    elif user == "paper" and comp == "scissors":
        print("Computer wins! Scissors cut paper.")

    elif user == "scissors" and comp == "paper":
        print("User wins! Scissors cut paper.")
    elif user == "scissors" and comp == "rock":
        print("Computer wins! Rock crushes scissors.")

    else:
        print("Invalid input. Please choose rock, paper, or scissors.")

    return user


while True:
    comp = random.choice(compChoice)
    user = validInput()
    if user == "exit":
        break
    result = rules(comp, user)
    print(result)
""" 
class RockPaperScissors:
    def __init__(self):
        self.compChoice = ["rock", "paper", "scissors"]
        
    
    def userInput(self):
        print("press 'Q' to quite..\n")
        print("Select Choice:\n1.Rock\n2.Paper\n3.Scissors")
        print()
        
        while True:
            usr = input("> ").lower()
            if usr in ["q", "rock", "paper", "scissors"]:
                return usr 
            print("Invalid Input..!")
    
    def rules(self, user, comp):
        if user == comp:
            print("It's a tie!")

        elif user == "rock" and comp == "scissors":
            print("User wins! Rock crushes scissors.")
        
        elif user == "rock" and comp == "paper":
            print("Computer wins! Paper covers rock.")

        elif user == "paper" and comp == "rock":
            print("User wins! Paper covers rock.")
        elif user == "paper" and comp == "scissors":
            print("Computer wins! Scissors cut paper.")

        elif user == "scissors" and comp == "paper":
            print("User wins! Scissors cut paper.")
        elif user == "scissors" and comp == "rock":
            print("Computer wins! Rock crushes scissors.")

        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

        return user, comp
        
    def play(self):
        
        while True:
            userChoice = self.userInput()
            if userChoice == "q":
                break
            result = self.rules(self.compChoice,userChoice)
            print(result)

startGame = RockPaperScissors()
startGame.play()