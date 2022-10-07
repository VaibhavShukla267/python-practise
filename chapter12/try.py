while(True):
    print("Press q to exit the game ")
    a=input("Enter a number")
    if a=='q':
        break
    try:
        print("I am Trying")
        if a>6:
            print("Your number is greater than 6 !!")
    except Exception as e:
        print(f"You entered a invalid input {e}")
        
print("Thanks fr playing the game!!!")
