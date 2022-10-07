class Employee:
    salary=1000
    salaryincre=1.2
    
    @property
    def salaryAfterIncrement(self):
        return self.salary * self.salaryincre
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
        self.salaryincre=sal/self.salary
        
e=Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=20000
print(e.salaryincre)
print(e.salary)
    