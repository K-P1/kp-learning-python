class Circle:

    def __init__(self, r):
        self.r = r

    def changeR(self,newR):
        self.r = newR

    def displayR(self):
        return self.r

    def calculateArea(self):
        return (22/7) * self.displayR() ** 2

    def calculatePerimeter(self):
        return 2 * (22/7) * self.displayR()


radius = float(input("Enter the Radius: "))
myCircle = Circle(radius)

while True:
    print("\nChoose any Option of your choice\n")
    print("1. Change Radius")
    print("2. Display Radius")
    print("3. Display Area")
    print("4. Display Perimeter")
    print("5. Quit\n")
    option = int(input("Enter the number corresponding to your option\t"))

    if option == 1:
        new_radius = float(input("Enter the new Radius: "))
        myCircle.changeR(new_radius)

    elif option == 2:
        print(f"The Radius of the Circle = {myCircle.displayR()}cm")
        
    elif option == 3:
        print(f"Area of Circle = {round(myCircle.calculateArea(),2)}cm squared")

    elif option == 4:
        print(f"Perimeter of Circle = {round(myCircle.calculatePerimeter(),2)}cm")

    elif option == 5:
        break

    else:
        print("Invalid Input")
