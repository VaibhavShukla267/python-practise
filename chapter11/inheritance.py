from asyncio.proactor_events import _ProactorBaseWritePipeTransport


class Employee:
    
    
    company="Google"
    
    
    def showDetails(self):
        print("This is an employee")




class Programmer(Employee):
    language="Python"
    company="Youtube"    
    def getLanguage(self):
        print(f"The Programmer Language is {self.language}")
    
    def showDetails(self):
        print("This Is an Programmer")



e=Employee()
e.showDetails()
p=Programmer()
print(e.company)
p.showDetails()
p.getLanguage()
print(p.company)

