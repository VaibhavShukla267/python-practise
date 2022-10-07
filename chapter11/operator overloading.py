class Number:
    def __init__(self,num1):
        self.num1 = num1

    
    def __add__(self,num2):
        print("Addition")
        return self.num1 + num2.num1
    
    def __mul__(self,num2):
        print("Multiply")
        return self.num1 * num2.num1
    
num1=Number(1)
num2=Number(2)
add=num1+num2
mul=num1*num2
print(add)
print(mul)