class Employee:
    company="Infoses"
    salary=40000
    salarybonus=60000
    
    
    @property   #property named as @property is called a getter method in which we  make a function to define attribute that will be changed in future
    def totalSalary(self):
        return  self.salary + self.salarybonus
    
    @totalSalary.setter   #property named @name.setter is done when we want to make a function but it will behave like  a property by using abstraction technique  
    def totalSalary(self, val):
        self.salary = val - self.salarybonus
        
e = Employee()
print(e.totalSalary)
e.totalSalary = 700000
print(e.salary)
print(e.salarybonus)