class Number:
    def __init__(self,num1):
        self.num1 = num1

    
    def __add__(self,num2):
        print("Addition")
        return self.num1 + num2.num1
    
    def __mul__(self,num2):
        print("Multiply")
        return self.num1 * num2.num1
    def __str__(self):
        return f"Decimal Number {self.num1}"
    def __len__(self):
        return 1
        
n=Number(9)    
print(n)
print(len(n))
