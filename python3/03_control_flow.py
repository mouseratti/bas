# operator if (bifurcation)
# single if
if True:
    print("this is true!")


# if-else construction
if True:
    print("1")
else:
    print("0")

# If the suite of an if clause consists only of a single line,
# it may go on the same line as the header statement.
if bool("non-empty string"): print("the condition isnt False")

########## Nested if statements
# but don't do this very often - it decreases readability and simply looks a bit ugly
var1 = 10*10

if var1 > 0:
    if var1 > 10:
        if var1 > 100:
            print("more than 100")
        elif var1 == 100:
            print("equals 100")
        else:
            print("less than 100")


# Python doesn't have switch-case operator, but it has elif

a = 10

if type(a) == float: print("float")
elif type(a) == str: print("str")
elif type(a) == int: print("integer")

elif type(a) == list:
    pass # python doesn't use braces so you need to use pass operator instead of emty {} block
else:
    print("some another type")



############## Loops

# WHILE
# A while loop statement in Python programming language
# repeatedly executes a target statement as long as a given condition is true.
#
# Here, statement(s) may be a single statement or a block of statements.
# The condition may be any expression, and true is any non-zero value.
# The loop iterates while the condition is true.
# When the condition becomes false, program control passes to the line immediately following
# the loop.
#
# In Python, all the statements indented by the same number of character spaces after
# a programming construct are considered to be part of a single block of code.
# Python uses indentation as its method of grouping statements.
counter = 0
while counter < 3:
    print("counter is ", counter)
    counter += 1

# If condition is false at the start, the loop will be passed
counter = 3
while counter < 3:
    print("counter is ", counter)
    counter += 1
assert counter == 3 # with an assert operator we can check the truth of the statement

# A loop becomes infinite if a condition never becomes FALSE.
# You must use caution when using while loops because of the possibility that this condition
# never resolves to a FALSE value. This results in a loop that never ends and blocks
# the program flow.
# Such a loop is called an infinite loop
# An infinite loop might be useful in client/server programming where the server needs to run
# continuously
# so that client programs can communicate with it as and when required.


# lets do "The Matrix"
import random
while 1: print(random.randint(0, 9))



# Loop control statements change execution from its normal sequence.
# When execution leaves a scope, all automatic objects that were created in
# that scope are destroyed.
while 1:
    random_number =random.randint(0, 9)
    if random_number == 9:
        print("Exiting..")
        break
    if random_number in range(0,2): continue
    print(random_number)



# while may be used with the else operator
counter = 0
while counter < 3:
    print("counter is ", counter )
    counter += 1
    # if counter == 2: break
else:
    print("loop has finished by the condition")



# FOR loop
for symbol in 'abc':
    print(symbol)

# you can get current index of the iterable sequence with enumerate function
# break, continue operators could be used too
for position, symbol in enumerate('abc', start=1):
    # if symbol.startswith('b'): continue
    # if symbol == 'c': break
    print(f"position is {position}, symbol is {symbol}")
else:
    print("loop is over")

