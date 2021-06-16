"""Write a program that will accept a number of days from the user than it will tell the user how many weeks and the remaining number of days that can be found in the number of days given"""
days = int(input("Enter number of days:\t"))
weeks = days // 7
remaining_days = days % 7
print("In ",days," days, we have ",weeks," weeks and ",remaining_days," days")
