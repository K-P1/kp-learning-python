"""
Use the web to determine the current world population
and the annual world population growth rate. Write an application that inputs these values,
then displays the estimated world population after one, two, three, four and five years.
"""
population = 7400000000
growthRate = 1.1

i = 1
while i <= 5:
    population += int((growthRate * population)/100)
    print(f"The population of the world will be {population} after {i} year(s)")
    i += 1
 
