a=int(input("Enter The Number:-"))
b=int(input("Enter the Number:-"))
try:
    c=a/b
except ZeroDivisionError:
    print("Infinite")
print(c)
