looping in python
loop is a sequence of instructions that is continually repeated until a certain condition is reached.
WHILE LOOP
with the while loop we can execute a set of statements as long as a condition is true.
example
x=1
while x<4:
    print(x)
    x+=1
**augmented assignment operator and inplace operator
** eval evalutes the input as a line of code
**every function in python has aheader and abody
the break statement:
with this break statement we can stop the loop even if the while condition is true,
the break keyword is used to exit/break outof a loop even if condiitions to be met are true
**pass or ... ignores the 'if' statement
    x=1
  while x<10:
      print(x)
      if x == 8:
          pass or ...
      a += 1
example
x=1
while x<10:
    print(x)
    if x == 8:
        break
    a += 1

THE ELSE STATEMENT
with the else statement we can run a  block of code once when the condition no longer is
true just like if statements; if all the above conditions are not met execute this command.