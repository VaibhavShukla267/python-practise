import random


def gamewin(you,comp):
    if comp==you:
            return None
    elif comp=='s':
        if you=='w':        
            return False
    elif comp=='w':
        if you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
    elif comp=='s':
        if you=='w':        
            return True
    elif comp=='g':
        if you=='w':
            return True
    elif comp=='s':
        if you=='g':
            return True
print("comp Turn:snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
        comp='s'
elif randNo==2:
        comp='w'
elif randNo==3:
        comp='g'
you=input("your Turn:snake(s) water(w) or gun(g)?")    
a= gamewin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a==None:
    print("The Game Is Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")