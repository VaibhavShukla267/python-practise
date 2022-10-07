from pickle import APPEND
from traceback import print_tb


a=[22,33,4,41,52,54,56,61,62,63,77,74,75]


#defination:-Ek majhedaar tareeka existing list se ek new list bannane ka.----------------------
#first method 
b=[]
for item in a:
    if item%2==0:
        b.append(item)

print(b)

#Shortcut Method
b=[i for i in a if item%2==0]
print(b)


        