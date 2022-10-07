class Employee:
    company="google"

    def getsalary(self):   #self is parameter that is pass automatically when we call a function
        print(f"salary for employee working in {self.company} is {self.salary}")


vaibhav=Employee()
vaibhav.salary=10000000
vaibhav.getsalary()#--------------------------or---------------------#Employee.getSalary(vaibhav)