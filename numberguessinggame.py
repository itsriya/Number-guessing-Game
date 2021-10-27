#Number Guessing game
"""
functions: main(): used to initialise the game
           play(): used for letting the player play the game"""
import random
def play():
    x=random.randint(1,100)
    limit=0
    flag=0
    user_input=input("Type easy or hard").lower()
    if(user_input=="easy"):
        limit=10
        print(f"you have {limit} chances")
    elif(user_input=="hard"):
        limit=5
        print(f"You have {limit} chances")

    while limit!=0:
        
        user=int(input("Guess the number:"))
        limit=limit-1
        if(user==x):
            print(f"You are right the number is{user}")
            flag=1
            break
        elif user>x:
            print("Too high")
        elif user<x:
            print("Too low")
        print(f"You have {limit} chances left")
    
    if flag==0:
        print("You lost the game")
        print(f" the number was{x}")

    elif flag==1:
        print("You won the game")
    

def main():
    logo= """
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/       \/            \/    \/     \/
        """
    print(logo)
    user_input=input("Do you want to play game(Y/N)?").lower()
    while user_input=='y':
        play()
        user_input=input("Do you want to play game(Y/N)?").lower()


main()
    
    
