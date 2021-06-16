"""
Write a program to print every number divisible by both 3 and 7 between 1 and 300.
"""

i = 1
while i <= 400:
    if i % 3 == 0 and i  % 7 == 0:
        print(f"{i} is a multiple of 3 and 7")
    i += 1
