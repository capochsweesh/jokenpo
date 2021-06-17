import os
import random

def main():

    list = ["rock", "paper", "scissors"]
    
    
    jokenpo = input('Rock, paper or scissors? ')
    
    if jokenpo in list:
        number = random.randint(0,2)
        result = list[number]
        print(result)
        
        #Rock : paper
        #paper : scissors
        #scissors : rock
        
        if jokenpo == result:
            print("That's a draw!")
        elif jokenpo == list[0] and result == list[1] or jokenpo == list[1] and result == list[2] or jokenpo == list[2] and result == list[0]:
            print("You lost!, retard")
        else:
            print("You won!")
    

if __name__ == "__main__":
    while(1):
        main()

os.system("pause")