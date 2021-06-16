python collections cont:
PYTHON SET
a set is a collection which is unordered and unindexed. in python sets are written
with curly brackets.
example
Q- create a set:
thisset= {4,10,15}
print(thisset)
output= {10,15,4} 
**note:
sets are unordered, so you cannot be sure in which order the items will appear.
LOOPING THROUGH SETS
you can loop through the set items using a for loop, or ask if a specified value
is present in a set, by using in keyword.
Example
thisset= {4,10,15}
for x in  thisset:
   print (x)
CHANGE ITEMS
once a set is created, you cannot change its items, but you can add new items.
-adding items
to add one item to a set use the add() method. to add more than one item to a set
use the update() method.
example
Q- add an item to this set
thisset= {4,10,15}
thisset.add("17")
print(thisset)
output=  {4,10,15,17}
Q- adding multiple items to a set
thisset= {4,10,15}
thisset.update([1,2,3,4])
print(thisset)
output= {4,10,15,1,2,3,4}

GET THE LENGTH OF A SET
to determine how many items a set has, use the len() method
example
Q-check the length of this set
thisset= {4,10,15}
len(thisset)
=3

REMOVE ITEM
to remove an item in a set, use the remove() or the discard() method.
example
thisset= {4,10,15}
thisset.remove("4")
print(thisset)
= {10,15}
if the item to be removed is not present the program will raise an error
-DISCARD METHOD
this does the same thing as remove but if the item to be removed is not present 
this wont raise an error.
-THE POP() METHOD
this returns the value of the removed item.
example
thisset= {4,10,15}
x=thislist.pop()
print(x)
=10 or 4 or 15
THE CLEAR() METHOD
the clear() method empties the set:
thisset= {4,10,15}
thisset.clear()
THE DEL KEYWORD
this deletes the list completly
JOINING TWO SETS
there are several ways to join two or more sets in python.
-the union method
you can use the union() method that returns a new set containing all items from
both sets, or the update() method that inserts all the items from one set into 
another:
example
set1={"a","b","c",}
set2={1,2,3}
set3= set.union(set2)
print(set3)
-the update method
this inserts the items in set2 into set1
set1={"a","b","c",}
set2={1,2,3}
set3= set.update(set2)
print(set3)
THE SE
*note both the union and update method will exclude any duplicate items
*there are other method that joinstwo sets and keep only the duplicates, or never the duplicate.
...
THE SET CONSTRUCTOR
it is also possible
