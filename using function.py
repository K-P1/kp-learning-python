"""
#Function Definition
def greeting():
    print("Good Morning")

#function Call
greeting(name, state, job,school)
"""
"""
def welfare(name):
    message = "Hello " + str(name) + ", How are you doing today?"
    print(message)

welfare("Soji")
"""
"""
from datetime import datetime
from datetime import date
from datetime import time

#day = date.today().weekday()

def day_of_the_week():
    day = date.today().weekday()
    if day == 0:
        weekday = "Monday"
    elif day == 1:
        weekday = "Tuesday"
    elif day == 2:
        weekday = "Wednessday"
    elif day == 3:
        weekday = "Thursday"
    elif day == 4:
        weekday = "Friday"
    elif day == 5:
        weekday = "Saturday"
    elif day == 6:
        weekday = "Sunday"

    print(f"Today is {weekday}")

day_of_the_week()
"""
"""
#x = int(input("Enter a number:\t"))
#y = int(input("Enter another number:\t"))

def maximum():
    x = int(input("Enter a number:\t"))
    y = int(input("Enter another number:\t"))
    if x > y:
        greater = x
    elif x< y:
        greater = y

    print(f"{greater} is the largest of {x} and {y}")

maximum()
"""
"""
x = "awesome"

def myfunc():
    global x
    #x = "Beautiful"
    print("Python is " + x)

def func2():
    print("Python is " + x)
myfunc()
func2()
""" """
pi = 3.142

def mute():
    pi += 0.1
    print(pi)
mute()"""
'''
write a program that will take in list as parameter. the list should contain\
name, address, profession, age and so on than add other stuff to the list
and print out the item in the list.
'''
profile = []
name = "Adedeji"
profile.append(name)
address = "Habert Mercury wau 17dfnuinoir/tnw"
profile.append(address)
profession = "Akpeja"
profile.append(profession)
age = 32
profile.append(age)

def print_profile(profile_list):
    print("Name = ", profile_list[0])
    print("Address = ", profile_list[1])
    print("Profession = ", profile_list[2])
    print("Age = ",profile_list[3])

print_profile(profile)

