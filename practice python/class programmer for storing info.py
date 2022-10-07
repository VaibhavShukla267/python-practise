class Programmer:
    company="Google"
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def getDetails(self):
        print(f"The name of the company is {self.company}  programmer is {self.name} working as a {self.position}")
    
vaibhav=Programmer("Vaibhav","Software Developer")
rohan=Programmer("Rohan","Software Engineer")
akash=Programmer("Akash","Project Manager")

vaibhav.getDetails()
rohan.getDetails()
akash.getDetails()