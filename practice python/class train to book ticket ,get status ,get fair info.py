class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    def getStatus(self):
        print("****************************************")
        print(f"The name of train is {self.name}"  )
        print(f"Number of seats available {self.seats} ")
    def fareInfo(self):
        print("******************************************")
        print(f"The price of tickets is {self.fare}")
    def Booktickets(self):
        print("******************************************")
        if (self.seats>0):
            print(f"Your seat is booked!! Yours seats number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("This Train is full try for another train!!")
print("Thank you for visiting our website ")
rajdhani=Train("Rajdhani Express",1,40000)
rajdhani.getStatus()
rajdhani.fareInfo()
rajdhani.Booktickets()
rajdhani.Booktickets()
rajdhani.getStatus()

        