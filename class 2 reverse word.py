"""
Write a python class that reverses a string
"""
#=====================================
class Word:

    def __init__(self,word):
        self.word = word

    def getWord(self):
        return self.word

    def setWord(self):
        newWord = input("Enter New Word")
        self.word = newWord

    def reverseWord1(self):
        #While loop
        reverse = ""
        count = len(self.getWord())-1

        while count != -1:
            reverse += self.getWord()[count]
            count -= 1

        return reverse


    def reverseWord2(self):
        #For Loop
        reverse = ""
        count = len(self.getWord())-1

        for x in range(len(self.getWord())-1,-1,-1):
            reverse += self.getWord()[count]
            count -= 1
            
        return reverse
#=======================================
word = input("Enter the Word: ")
wordClass = Word(word)

while True:
    print("\nChoose any Option of your choice\n")
    print("1. Change Word")
    print("2. View Word")
    print("3. Reverse Word Using While Loop")
    print("4. Reverse Word using For Loop")
    print("5. Quit\n")
    option = int(input("Enter the number corresponding to your option\t"))

    if option == 1:
        wordClass.setWord()

    elif option == 2:
        print(f"The word available = {wordClass.getWord()}")
        
    elif option == 3:
        print(f"While Loop Reverse = {wordClass.reverseWord1()}")

    elif option == 4:
        print(f"For Loop Reverse = {wordClass.reverseWord2()}")

    elif option == 5:
        break

    else:
        print("Invalid Input")

        
        
