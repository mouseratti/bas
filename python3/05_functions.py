"""
A function is a block of organized, reusable code that is used to perform a single, related action.
 Functions provide better modularity for your application and a high degree of code reusing.
 As you already know, Python gives you many built-in functions like print(), len, max etc.
 but you can also create your own functions. These functions are called user-defined functions.

 Defining a Function
You can define functions to provide the required functionality.
Here are simple rules to define a function in Python.

Function blocks begin with the keyword def followed by the function name
and parentheses ( ( ) ).

Any input parameters or arguments should be placed within these parentheses.
You can also define parameters inside these parentheses.

The first statement of a function can be an optional statement -
the documentation string of the function or docstring.
The code block within every function starts with a colon (:) and is indented.

The statement return [expression] exits a function,
optionally passing back an expression to the caller.
A return statement with no arguments is the same as return None.

Syntax
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
By default, parameters have a positional behavior and you need to inform them in the same order
that they were defined.
"""


def print_me(inputted):
    "This prints a passed string into this function"
    print(inputted)
    return


# Now you can call printme function
print_me("I'm first call to user defined function!")
print_me("Again second call to the same function")


# Pass by reference vs value
# All parameters (arguments) in the Python language are passed by reference.
# It means if you change what a parameter refers to within a function,
# the change also reflects back in the calling function. For example −

# Function definition is here
def modify_me(mylist=[]):
    "This changes a passed list into this function"
    mylist.extend([1, 2, 3, 4])
    # mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return


# Now you can call function
mylist = [10, 20, 30]
modify_me(mylist)
print("Values outside the function: ", mylist)
modify_me();
modify_me()  # check the results - they are different

# Function Arguments
# You can call a function by using the following types of formal arguments −
#
#   Required arguments
#   Keyword arguments
#   Default arguments
#   Variable-length arguments

# Required arguments
# Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function definition.
#
# To call the function print_me(), you definitely need to pass one argument,
# otherwise it gives a syntax error as follows −
print_me()


# Keyword arguments
# Keyword arguments are related to the function calls.
# When you use keyword arguments in a function call,
# the caller identifies the arguments by the parameter name.
#
# This allows you to skip arguments or place them out of order because
# the Python interpreter is able to use the keywords provided to match the values with parameters.
def printinfo(name, age):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return


printinfo(age=50, name="miki")


# Default arguments
# A default argument is an argument that assumes a default value if a value is not provided in the function
# call for that argument.
def printinfo(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
printinfo('Mikhail', 31)
printinfo(name="Azat")



# Variable-length arguments
# You may need to process a function for more arguments than you specified while defining the function.
# These arguments are called variable-length arguments and are not named in the function definition,
# unlike required and default arguments.
#
# Syntax for a function with non-keyword variable arguments is this −

# def functionname([formal_args,] *var_args_tuple ):
#     "function_docstring"
#     function_suite
#     return [expression]
# An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable
# arguments. This tuple remains empty if no additional arguments are specified during the function call.

def print_args( arg1, *args ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print(type(args))
    for var in args:(print(args))
    return args

# Now you can call printinfo function
print_args( 10 )
print_args( 70, 60, 50 )
