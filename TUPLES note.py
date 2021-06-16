TUPLES
a tuple is a collection which is ordered and unchangeable. they are written with round 
bracket. one major diffrence between a list and a tuple is that a tuples are immutable.
example
thistuple= ("ayo",""kunle","temi","jide")
print(thistuple)

ACCESSING TUPLES ITEMS
you can access tuple items by referring to the index number just like in list,
inside square brackets
example
thistuple= ("ayo",""kunle","temi","jide")
print(this tuple[1])
output "kunle"

NEGATIVE INDEXING
this means beggining from the end just like in list, -1 refers to the last item,
-2 refers to the second to the last item and so on.
example
thistuple= ("ayo",""kunle","temi","jide")
print(thistuple[-1])
output= "jide"

RANGE OF INDEXES
you can specify a range of indexes by specifying where to start and where to 
end the range just like in list.
when specifying a range, the return value will be a new tuple with the specified
items.
example
thistuple= ("ayo","kunle","temi","jide")
print(thistuple[0:2])
output= "ayo","kunle","temi"

RANGE OF NEGATIVE INDEXES
specify negative indexes if you want to start the search from the end of the
tuple just like you will in list.
example
thistuple= ("ayo","kunle","temi","jide")
print(thistuple[-1:-3])
output="jide","temi","kunle"

CHANGING TUPLES VALUE
once a tuple has been created, the values cannot be changes.
but there is a walkaround to changing the values:
-coverting to a list
-then
-converting back to a tuple
example
x= ("ayo","kunle","temi","jide")
y=list(x)
y[1]="dayo"
x=tuple(y)
print(x)
output= ("ayo","dayo","temi","jide")

LOOPING IN TUPLE
you can loop through the tuple item by using a for loop.
example
thistuple= ("ayo","kunle","temi","jide")
for x in thistuple:
  print(x)

CHECK IF ITEM EXIST
to check for a particular item in a tuple use the keyword:
example
Q- check if oyin is present in thistuple
thistuple= ("ayo","kunle","temi","jide")
if "oyin" in thistuple:
  print("yes oyin is in the thistuple")
else:
    print("oyin is not in this tuple")

TUPLE LENGTH
to determine how many items are in a tuple, use the len() method:
thistuple= ("ayo","kunle","temi","jide")
print(len(thistuple))
output= 4

ADD ITEMS
once a tuple is created, nothing can be added or removed because they are unchangeble.
-coverting to a list
-edit the list then
-converting back to a tuple
example
x= ("ayo","kunle","temi","jide")
y=list(x)
y.apppend(dayo)
x=tuple(y)
print(x)
output= ("ayo","kunle","temi","jide","dayo")

CREATING TUPLE WITH ONE ITEM
this is done by adding a comma after the tuple value
example
thistuple= ("ayo",)

DEL KEYWORD IN TUPLES
the del keyword can be used to delete all the values in a tuple
example
thistuple= ("ayo","kunle","temi","jide")
del thistuple


JOINING TWO TUPLES
 to join two or more tuples you can use the + operators:
example
tuple1=("a","b","c")
tuples2=(1,2,3,4)
tuples3= tuple1 + tuple2
print(tuple3)


THE TUPLE CONSTRUCTOR
it is possibke to use the tuple() constructor to make a tuple,
example
thistuple= ("ayo","kunle","temi","jide")
thistuple= (("ayo","kunle","temi","jide"))
both are correct


TUPLES METHODS
-count(): this returns the number of times a values occurs in the tuple
-index(): this returns the index of the value provided in the tuple