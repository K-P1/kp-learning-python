"""if 2 % 2 == 0:
    print("2 is an even number")
else:
    print("2 is an odd Number")
"""
"""number = int(input("Enter any Whole number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd Number")"""


number = int(input("Enter any Whole number: "))
if number % 2 == 0:
    print(f"{number} is an even number", end = " ")
    if number % 4 == 0:
        print(f"and {number} is a multiple of 4")
    else:
        print(f"but {number} is not a multiple of 4")
else:
    print(f"{number} is an odd Number", end = " ")
    if number % 5 == 0:
        print(f"and {number} is a multiple of 5")
    else:
        print(f"not {number} is not a multiple of 5")
