import random
randomNo=random.randint(1,100)

userGuesses=None
Guesses=0
while(userGuesses!=randomNo):
    userGuesses=int(input("Enter The No. : "))
    Guesses+=1
    if(userGuesses==randomNo):
        print("You Guessed The correct Number!!")
    if(userGuesses>randomNo):
        print("Enter The Smaller Number!!")
    else:
        print("Enter The Greater Number!!")    
        
print(f"You Guessed The number in {Guesses} !!")