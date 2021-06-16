python collections
there are 4 collection data type in the python programming language:
LIST- this us a collection which iss ordeered and chageable. allows duplicate members.
TUPLE- is a collection which is ordered and unchangeable. allows duplicate members.
SET-
DICTIONARY-

LIST
A list is a collection which is ordered and changeable. in python list are written with square
brackets.
CREATE A LIST
 thislist= ["apple","banana","cherry"]
print(thislist)
ACCESSING ITEMS USING THE INDEX NUMBER
Q- print the second item of the list
thislist= ["apple","banana","cherry"]
thislist[1]
output="banana"
NEGATIVE INDEXING
this means starting from the end,-1 refers to the last item,-2 refers to the second 
to the last item.
example

*in indexing the upper band is not included
*itration means going trough a set of characters
*loop means repeting an action
*muteable mean you can change a character in place
*immuteable 
RANGE OF INDEX
you can specify a range of indexes by specifying where to start ad where to end 
the range, when specifying a range, the return value will be a new list wuth the 
specified items.
example:
thislist= ["apple","banana","cherry"]
thislist[-2:-1]
output=['banana']

CHANGE ITEM VALUE
to change item value of a specific item, refer to the index number.
example:
thislist= ["apple","banana","cherry"]
thislist[1]= "blackcurrant"
output will be ["apple","blackcurrant","cherry"]


ADDING ITEM TO LIST
-insert() method:
example
thislist= ["apple","banana","cherry"]
thislist.insert(1,"orange")

REMOVE ITEM
-remove() method:
removes the specified item
example
thislist= ["apple","banana","cherry"]
thislist.remove("banana")
print this list= ["apple","cherry"]

-the pop() method
this removes the specified index, or  the last item, if the list is not specified.
example
thislist= ["apple","banana","cherry"]
thislist.pop
will give ["apple","banana"]

CHECK IF ITEM EXIST
to determine if a specific item is present in alist use the in keyword.
example
Q- check if apple is in this list
>>> thislist= ["apple","banana","cherry"]
>>> if "apple" in thislist:
	print("apple is there")
output= apple is there

THE DEL KEYWORD
this removes a specified index
example
thislist= ["apple","banana","cherry"]
del thislist[0]
output= ["banana","cherry"]
*the del keyword can also delete the list completly:
thislist=["banana","cherry"]
del thislist
*this deletes all the value stored in thislist
** a list in python can contain diffrent data types at a time

