ages = [21, 18, 17, 21, 20, 26, 28, 25]
'''
check = int(input("What age are you looking for:  "))
if check in ages:
    print("Sure, we have what you are looking for")
else:
    print("Sorry, Age is not present")
'''
facltrAges = [40, 35, 43, 16]

ages = ages.extend(facltrAges)
print(ages)

