maths=int(input("Enter The Marks:"))
physics=int(input("Enter The Marks:"))
chemistry=int(input("Enter The Marks:"))


if(maths<33 or physics<33 or chemistry<33):
    print("you are fail!!")
elif(maths+physics+chemistry)/3<40:
    print("you are fail!!")

else:
    print("congratulations you are pass!!")