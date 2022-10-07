import random 


def gamewin(comp,you):
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
    elif comp=='w':
       if you=='s':
        return True
    elif comp=='g':
        if you=='w':
            return True
    elif comp=='s':
        if you=='g':
            return True
print("comp turn : snake(s) water(w)  gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
     comp='g'
you = input(" snake(s) water(w) gun(g) ?")
a=gamewin
print(f"you choose {you}")
print(f"comp choose {comp}")
if a==None:
    print("The Is Tie!!")
elif a==True:
    print("You Won!!")
elif a==False:
    print("You Lose!!")
    
            