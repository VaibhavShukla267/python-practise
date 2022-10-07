try:
    a=int(input("Enter the first number "))
    b=int(input("Enter second number"))
    c=a/b
    print(c)
except ValueError as e:
    print("Please Enter valid value")
except ZeroDivisionError as e:
    print("You have divided the number by 0")
print("Thanks playing this game!!")
