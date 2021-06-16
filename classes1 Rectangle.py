"""
Write a python class named rectangle constructed by a length and width
and a method which will will compute the area and perimeter of the
rectangle
"""
#========================================
class Rectangle:

    #Constructor Method
    def __init__(self, length, width):
        self.x = length
        self.y = width

    #Setter Methods/ Mutator Method
    def setX(self,newX):
        self.x = newX

    def setY(self,newY):
        self.y = newY

    #Accessor Methods/Getters
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #Action Methods
    def getArea(self):
        area = self.getX() * self.getY()
        return area

    def getPerimeter(self):
        per = 2 * (self.getX() + self.getY())
        return per

#====================================
a = float(input("Enter the Length of the rectangle: "))
b = float(input("Enter the Width of the rectangle: "))
myRectangle = Rectangle(a,b)

while True:
    print("\nChoose any Option of your choice\n")
    print("1. Change Length")
    print("2. Change Width")
    print("3. View Length")
    print("4. View Width")
    print("5. Calculate Area")
    print("6. Calculate Perimeter")
    print("7. Quit\n")
    option = int(input("Enter the number corresponding to your option\t"))

    if option == 1:
        newLength = float(input("Enter the value for the new length"))
        myRectangle.setX(newLength)

    elif option == 2:
        newWidth = float(input("Enter the value for the new Width"))
        myRectangle.setY(newWidth)

    elif option == 3:
        print(f"Length of Rectangle = {myRectangle.getX()}cm")
        
    elif option == 4:
        print(f"Width of Rectangle = {myRectangle.getY()}cm")

    elif option == 5:
        print(f"Area of Rectangle = {myRectangle.getArea()}cm")

    elif option == 6:
        print(f"Perimeter of Rectangle = {myRectangle.getPerimeter()}cm")

    elif option == 7:
        break

    else:
        print("Invalid Input")
