"""
(Assign grades) Write a program that reads a list of scores and then assigns grades
based on the following scheme:
The grade is A if score is best – 10.
The grade is B if score is best – 20.
The grade is C if score is best – 30.
The grade is D if score is best – 40.
The grade is F otherwise.
"""
#Request for max score
best = int(input("Enter Maximum score:  "))
#get list of scores
scores = input("Enter scores(seperate each score with a space):   ")
scoreList = scores.split()          #split scores string into  a list

#repeat for every score entered
for x in range(len(scoreList)):
    score = int(scoreList[x])       #convert every score string to an integer
    if score <= best and score >= 0:
        if score >= best - 10:
            grade  ='A'                    #grade is 'A' if
        elif score >= best - 20:
            grade = 'B'
        elif score >= best - 30:
            grade = 'C'
        elif score >= 40:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Student {x} score is {score} and grade is {grade}")
    else:
        print("Invalid score")          #score is not valid if it is not between 0 and the max score

"""
2. Write a program that reads a list of integers and
displays them in the reverse order in which they were read.
"""

#get list of numbers
nums = input("Enter a list of integers(seperate integers with a space):   ")

#split the number string and reverse the list
numList = nums.split()
numList.reverse()

#iterate through the numList and print each numbers ending with space
for num in numList:
    print(num, end=' ')


"""
3. (Count occurrence of numbers) Write a program that reads some integers
between 1 and 100 and counts the occurrences of each.
"""
#get list of numbers
nums = input("Enter a list of integers(seperate integers with a space):   ")

#split the number string and reverse the list
numList = nums.split()

numsDistinct = []
for num in numList:
    if int(num) not in  numsDistinct:
        numsDistinct.append(int(num))

print(numsDistinct)
