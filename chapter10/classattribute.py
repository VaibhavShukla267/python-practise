class Employee:
    company="Google"

harry = Employee()
vaibhav = Employee()
print(harry.company)
print(vaibhav.company)
Employee.company = "youtube"
print(harry.company)
print(vaibhav.company)
