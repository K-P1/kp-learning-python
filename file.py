import os

path1 = r"C:\Users\CHRIS HALOGEN\Desktop\genesis python Bootcamp\app_users"
"""
filename = "new2.txt"
full_file_path = os.path.join(path1,filename)

file = open(full_file_path, "wt")
file.write("Hello")
file.write("How are you")
file.close()
"""
for element in os.listdir(r"C:\Users\CHRIS HALOGEN\Desktop"):
    print(element)
