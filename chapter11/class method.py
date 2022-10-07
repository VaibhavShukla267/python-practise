class Employee:
    company="Infoses"
    salary=100000
    location ="Kanpur"
    
    #def changesalary(self,sal):
     #   self.__class__.salary=sal #-----------------___class__ ko dunder class bolte hy ye class me koi change krna ho to ye use kr sakte hy---------------
        
    @classmethod
    def changesalary(cls,sal):  #---also called decorator--------------@class method ek duusra tareka hy class ke koi attribute ki value change krne ka-----------
        cls.salary=sal
        
e=Employee()    
print(e.salary)
e.changesalary(4000000000)
print(e.salary)
print(e.salary)
            
