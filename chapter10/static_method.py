class Employee:
    company="google"
    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
    
    
    @staticmethod       #if you don't use self you have to use static method     
    def greet():
        print("Good Morning sir Have a nice day!! ")
        
vaibhav=Employee()
vaibhav.salary= 10000000000
vaibhav.getsalary("Thanks!!")#Employee.getsalary(vaibhav)
vaibhav.greet()   #Employee.greet()