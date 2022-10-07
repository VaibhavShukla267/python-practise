#formula (a+ib)(c+id)=(ac-bd) + (ad+bc)i multiplication ke liye


class Complex:
    
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
        
    def __add__(self,c):
        return Complex(self.real+c.real , self.imaginary+c.imaginary)
    
    def __mul__(self,c):
        mulreal=self.real*c.real - self.imaginary*c.imaginary
        mulimag=self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulreal,mulimag)
        
    def __str__(self):     
        return f"{self.real} + {self.imaginary}i" 

        
c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)
print(c1*c2)
    

        