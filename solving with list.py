'''
Forty students were asked to rate the quality of the food in the student cafeteria on a
scale of 1 to 10 (1 means awful and 10 means excellent). Place the 40 responses in an
integer array and summarize the results of the poll.
'''
import random
responses = []
rate1 =  0
rate2 = 0
rate3 = 0
rate4 =  0
rate5 = 0
rate6 = 0
rate7 =  0
rate8 = 0
rate9 = 0
rate10 = 0

for x in range(40):
    rndNum = random.randint(1, 10)
    responses.append(rndNum)

for x in responses:
    if x == 1:
        rate1 += 1
    elif x == 2:
        rate2 += 1
    elif x == 3:
        rate3 += 1
    elif x == 4:
        rate4 += 1
    elif x == 5:
        rate5 += 1
    elif x == 6:
        rate6 += 1
    elif x == 7:
        rate7 += 1
    elif x == 8:
        rate8 += 1
    elif x == 9:
        rate9 += 1
    elif x == 10:
        rate10 += 1
        
print(f"Total response for Awful = {rate1}")
print(f"Total response for rate2 = {rate2}")
print(f"Total response for rate3 = {rate3}")
print(f"Total response for rate4 = {rate4}")
print(f"Total response for rate5 = {rate5}")
print(f"Total response for rate6 = {rate6}")
print(f"Total response for rate7 = {rate7}")
print(f"Total response for rate8 = {rate8}")
print(f"Total response for rate9 = {rate9}")
print(f"Total response for Excellent = {rate10}")



