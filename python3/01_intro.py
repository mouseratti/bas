# how to create a new variable
# new_var is just a link to integer object storing value 1
new_var = 1

string_var = 'new string variable'
string_var.upper()

# multiple assignment
# Python allows you to assign a single value to several variables simultaneously
# But if variable is mutable, it could be a problem
a = b = c = 1

# Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively,
# and one string object with the value "john" is assigned to the variable c.
a,b,c = 1,2,"john"


new_var == 1 # how to compare two integers

new_var == string_var # this is False, because of different types


new_var > string_var # TypeError


print(new_var, string_var, "another unassigned string object")

"""
This is value read from stdout. Type of this inputted value is always str!
"""
string_from_input = input("insert any value and press Enter: ")

