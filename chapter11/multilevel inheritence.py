class Person:
    Nation="India"
    def takeBreak(self):
        print("I am Sleeping..........Don't Disturb Me!!!")



class Employee(Person):
    company="Infoses"
    def getSalary(self):
        print("My Salary is $10000k")
    def takeBreak(self):
        print("I have No time to sleep...........So No Break Only Work!!!!")
    
    
class Programmer(Employee):
    name="Vaibhav Shukla"
    company="Fiverr"
    def takeBreak(self):
        print("I Earn soo much so I can take it anytime!!!!!!")
    def getSalary(self):
        print("I Earn Infinite Dollors")


p=Person()
e=Employee()
pr=Programmer()
print(pr.name)
print(pr.Nation)
print(e.company)
pr.getSalary()
pr.takeBreak()


