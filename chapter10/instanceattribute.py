class Employee:
    company="google"
    salary=100#=------------------agar instance me koi value nhi hy to class ka print hoga
harry=Employee()
vaibhav=Employee()
harry.salary=300
vaibhav.salary=400#--------phle instance attribute print hota hy
print(harry.company)
print(harry.salary)
print(vaibhav.company)
print(vaibhav.salary)
#print(vaibhav.address)#---------------throws error because there is nothing in instance and class attribute