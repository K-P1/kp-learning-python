i=0
num =0
def lists(test):
    global i
    global num
    if type(test[i])==list:
        for obj in test[i]:
            num =num + obj
    else:
        num=num + test[i]
    if i < len(test)-1:
        i += 1
        return lists(test)
    else:
        return num
test=[1,2,[3,4],[5,6]]
print(lists(test))
