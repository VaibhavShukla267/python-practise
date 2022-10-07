class Calculator:
    
    def __init__(self,num):
         self.number=num
    def square(self):
        print(f"The Square Of {self.number} is {self.number **2}")
    def cube(self):
        print(f"The Cube Of {self.number} is {self.number **3}")
    def squareroot(self):
        print(f"The Square Root Of {self.number} is {self.number **0.5}")
    @staticmethod
    def greet():
        print("hello")
#a=Calculator( num=print(int(input("Enter The Number"))))
a=Calculator(2)
a.square()
a.cube()
a.squareroot()
a.greet()
