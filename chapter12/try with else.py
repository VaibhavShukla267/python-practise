from tokenize import Number


try:
    i=int(input("Enter A Number: "))
    i=1/i
except Exception as e:
    print(e)
else:
    print("This program is successful")
    
