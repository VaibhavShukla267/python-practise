class Employee:
    company="Infoses"
    eCode=120
    salary = 10000000000
    def getSalary(self):
        print(f"The salary of Employee is {self.salary}")
class Freelancer:
    company="Fiverr"
    Level=0
    
class Programmer(Employee,Freelancer):#-----------------isme infoses iss liya phle access kiya kyuki hm employee vaali class ko phle likha hy 
    name="Vaibhav"
    
    
p=Programmer()
print(p.name)
print(p.company)
p.getSalary()