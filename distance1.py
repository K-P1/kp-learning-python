"""
---------------------------15 mins----------------------------
Imagine we live in a 3D world, write a class constructed by the 3D co-
ordinates of a taxi driver and a client. The class should be able to tell the
distance between the driver and the client as a crow flies
"""
import random as rnd

class Distance:

    #Constructor Method
    #Point1 = Driver
    #point2 = Client
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    #Accessors
    def getPoint1(self):
        return self.point1

    def getPoint2(self):
        return self.point2

    #Mutators
    def changePoint1(self,new_point):
        self.point1 = new_point

    def changePoint2(self,new_point):
        self.point2 = new_point

    #Action Methods
    def getDistance(self):
        first_term = (self.getPoint1()[0] - self.getPoint2()[0]) ** 2
        second_term = (self.getPoint1()[1] - self.getPoint2()[1]) ** 2
        third_term = (self.getPoint1()[2] - self.getPoint2()[2]) ** 2

        distance = (first_term + second_term + third_term) ** (0.5)
        distance = round(distance,2)

        return distance


clientx = rnd.randint(1,100)
clienty = rnd.randint(1,100)
clientz = rnd.randint(1,100)
driverx = rnd.randint(1,100)
drivery = rnd.randint(1,100)
driverz = rnd.randint(1,100)

point = Distance([driverx,drivery,driverz],[clientx,clienty,clientz])

while True:
    print("\nChoose any Option of your choice\n")
    print("1. Change Co-ordinates of Driver")
    print("2. Change Co-ordinates of Clients")
    print("3. Display Co-ordinates of Driver")
    print("4. Display Co-ordinates of Clients")
    print("5. Display Distance between Client and Driver")
    print("6. Quit\n")
    option = int(input("Enter the number corresponding to your option\t"))

    if option == 1:
        newdriverx = rnd.randint(1,100)
        newdrivery = rnd.randint(1,100)
        newdriverz = rnd.randint(1,100)
        point.changePoint1([newdriverx,newdrivery,newdriverz])

    elif option == 2:
        newclientx = rnd.randint(1,100)
        newclienty = rnd.randint(1,100)
        newclientz = rnd.randint(1,100)
        point.changePoint2([newclientx,newclienty,newclientz])
        
    elif option == 3:
        print(point.getPoint1())

    elif option == 4:
        print(point.getPoint2())
        
    elif option == 5:
        print(f"The distance between the client and the driver is\
              {point.getDistance()}m")
    elif option == 6:
        break
    else:
        print("Invalid Input")

        








        
