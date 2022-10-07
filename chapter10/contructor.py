class Employee:
    company="google"
    def __init__(self,name,company,salary,subunit):
        self.name=name
        self.company=company
        self.salary=salary
        self.subunit=subunit
        print("Employee created")
    def getDetail(self):
        print(f"The name of Employee {self.name} ")
        print(f"The name of company is {self.company}")
        print(f"Salary of Employee {self.salary} ")
        print(f"Name of subunit {self.subunit}")

    def greet(self):
        print("Good morning sir have a nice day!!")

vaibhav=Employee("Vaibhav","Google",100000,"Youtube")
vaibhav.getDetail()
vaibhav.greet()        