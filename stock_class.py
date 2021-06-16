"""
-----------------------------20 mins---------------------------------
Design a class to represent a company's stock constructed by stock key,
(# followed by 8 alpha numeric characters), initial price, current price.
The class should be able to show percentage change in price and tell if
there is an appreciation or depreciation in value of stock
"""
import random
alphaNumerics = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#Definiton of the stock class
class Stock:

    #Constructor method
    def __init__(self, initPrice, currPrice):

        #Assigns a generated stock key to the stockkey attribute of the class
        self.__stockKey = self.genStockKey()
        
        self.__initPrice = initPrice
        self.__currPrice = currPrice

    #Generate 9 random alphaNumeric characters as stockKey
    def genStockKey(self):
        stockKey = '#'
        for x in range(8):
            stockKey += random.choice(alphaNumerics)
            
        return stockKey

    #Accessor Methods

    #returns stock key
    def getStockKey(self):
        return self.__stockKey

    #returns initial price
    def getInitPrice(self):
        return self.__initPrice

    #returns current price
    def getCurrPrice(self):
        return self.__currPrice


    #returns percentage change in price    
    def getPerChange(self):
        diff = self.__initPrice - self.__currPrice
        perChange = abs(diff)/self.__initPrice * 100
        return perChange

    #tells if stock price has appreciated or otherwise
    def getPriceStatus(self):
        diff = self.__initPrice - self.__currPrice
        if diff < 0:
            return 'Appreciated'
        elif diff > 0:
            return 'Depreciated'
        else:
            return 'Unchanged'

    
    #Mutator Methods

    #sets initial price
    def setInitPrice(self, initPrice):
        self.__initPrice = initPrice

    #sets current price
    def setCurrPrice(self, currPrice):
        self.__currPrice = currPrice

   
ferrari = Stock(400000, 750000)
print(ferrari.getStockKey())
print(f'{ferrari.getPerChange()}%')
print(ferrari.getPriceStatus())



        
