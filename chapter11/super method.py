class Person:
    Nation="India"
    def __init__(self):
        print("Initializing Person")
    def takeBreak(self):
        print("I am Sleeping..........Don't Disturb Me!!!")



class Employee(Person):
    company="Infoses"
    def getSalary(self):
        print("My Salary is $10000k")
    def __init__(self):
        super().__init__()
        print("Initializing Employee")
    def takeBreak(self):
        super().takeBreak()
        print("I have No time to sleep...........So No Break Only Work!!!!")
    
    
class Programmer(Employee):
    name="Vaibhav Shukla"
    company="Fiverr"
    def takeBreak(self):
        super().takeBreak()
        print("I Earn soo much so I can take it anytime!!!!!!")
    def __init__(self):
        super().__init__()
        print("Initializing Programmer")
    def getSalary(self):
        print("I Earn Infinite Dollors")


p=Person()
p.takeBreak()
e=Employee()
e.takeBreak()
pr=Programmer()
pr.takeBreak()


