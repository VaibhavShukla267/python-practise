from ast import Num


num=int(input("Enter The Number:"))

for i in range(2,num):
    if(num%i==0):
        print("The number is prime!!")
    else:
        print("The number is not prime!!!")

