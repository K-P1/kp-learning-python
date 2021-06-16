"""
Name:  Salaudeen Ahmad
Instructors Name: Olusoji
question 1:  Write a program that implements the count method of a string, i.e ask user for an input, then count
the number of occurences of a certain letter.
"""

line = input("Enter a line:  ")
searchIdx = input("Enter a letter to check its count in your line: ")

count = 0
i = 0
len = len(line)

while i < len:
    if line[i].upper() == searchIdx.upper():
        count += 1
    i += 1

print(f"{searchIdx} occured {count} times")
