"""
Write a python class that checks for palindrome
Note:A palindrome is a word that reads backwards the same way it reads
forward 
"""

class Palindrome:

    def __init__(self,string):
        self.__word = string

    def getWord(self):
        return self.word

    def reverseWord(self):
        count = len(self.getWord()) - 1
        reverse = ""

        for i in range(len(self.getWord()) - 1, -1, -1):
            reverse+= self.getWord()[count]
            count += 1

        return reverse

    def check(self):
        if self.getWord() == self.reverseWord():
            print("{self.getWord()} is a Palindrome")
        else:
            print(f"{self.getWord()} is not a Palindrome")


        
