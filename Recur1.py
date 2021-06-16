my_file=open("demo text.txt")  #locate text from file
read_my_file=my_file.readline() #read a paragragh
no_of_my_file=read_my_file.count(" ") + 1 #add one to spacecount to give word
                                            #count



def numFile(fileNo): #function with one parameter
    if fileNo==0:   #ends execution when parameter reaches zero
        return 0
    else:
        return numFile(fileNo-1) + 1   #add number of words
print(numFile(no_of_my_file))       #print number of words
