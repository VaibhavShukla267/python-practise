import random
def gameWin(comp,you):
    if comp==you:
        print("The game is tie")
        return None
    elif comp=='s':
        if you=='w':
            return False
    elif comp=='g':
        if you=='s':
            return False
    elif comp=='w':
        if you=='g':
            return False
    elif comp=='w':
        if you=='s':
            return True
    elif comp=='s':
        if you=='g':
            return True
    elif comp=='g':
        if you=='w':
            return True
print("Comp Turn:Snake(s),Water(w),Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=(input("Your Turn = Sanke(s),Water(w),Gun(g)? "))
a=gameWin(comp,you)
print(f"Computer Choose {comp}")
print(f"You Choose {you}")
if a==None:
    print("The Game is tie")
elif a==True:
    print("You Won The Game")
else:
    print("You Lose")
print("Thanks for playing this game")
    
    
    