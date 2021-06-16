"""Write a program that takes radius as input and prints out the area and the perimeter properly"""
radius = float(input("Enter the radius:\t"))
area = 22/7*radius**2
perimeter = 44/7*radius
print("Area = " + str(area) + "cm squred")
print("Perimeter = " + str(perimeter) + "cm")

#or

print("Area =",area,"cm squared")
print("Perimeter =", perimeter,"cm")

#or Using Formatted strings

print(f"A circle of radius {radius}cm will have a perimeter of {perimeter}cm and an area of {area}cm squared")
