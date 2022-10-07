from math import factorial


num=int(input("Enter the number:"))

factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The Factorial Of {num} is{factorial}")
    
