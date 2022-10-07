class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
vaibhavapplication=RailwayForm()
vaibhavapplication.name="Vaibhav"
vaibhavapplication.train="rajdhani express"

vaibhavapplication.printData()