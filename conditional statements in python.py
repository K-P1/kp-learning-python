conditional statement in python:
this performs different computations or actions depending on whatever a specific boolean expression evaluaates to true or false.
they are handled by if statements in python.
from maths:
equals: a==b
not equals: a != b
less than: a<b
greater than: a>b
greater than or equals to: a>=b

example of if statement:

ade_height= 6.25
oyin_height= 5.75
if ade_height > oyin_height:
    print("ade is taller tham oyin")

The elif keyword:

the elif keyword is python way of saying "if the previous condition were not true, then try this condition"
example-
boys score=24.77
girls score=25.01
if boys score>girls score:
    print("boys win, girls lose")
elif girls score>boys score:
    print("girls win, boys lose")

the else keyword:

if 
the else keyword catches anything which isnt caught by the preceding conditions.
example-
#program to calc the longer journey
#between lagos-ibadan and lagos london
lb_max_time=2.5
ll_max_time=6
if lb_max_time>ll_max_time:
    print("lagos to ibadan takes more time")
elif lb_max_time<ll_max_time:
    print("lagos to london takes more time")
else:
    print("both take equal time")

using logical operators:
you can use operators 'and,or and not' in python conditional statements.
for example:
x=200
y=33
z=500
if x> y and z>x:
  print("both condition are true")


the pass keyword
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
example
boys=17
if boys==17:
    pass
