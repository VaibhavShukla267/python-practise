from traceback import print_tb


def greet(name):
    print(f"Good Morning {name}")


#print(__name__)
if __name__=="__main__":#---this behaviour is used to check wether the file is ran directly or imported to another file.-----------
    
    n=input("Enter the name")
    greet(n)
    