i=0
largest=0
def larger(test):
    global i
    global largest
    if int(test[i])>largest:
        largest = int(test[i])
    if i < len(test)-1:
        i += 1
        return larger(test)
    else:
        return largest
print(larger("1234567828"))
    
