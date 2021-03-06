######## NoneType
a = None
a is None  # both objects are the same!
a == None


# boolean vars
bool_var = True
bool_var  == True

bool_var = not True
False and print("True") # boolean operations are lazy!
False or print("True")

# some values can be implicitly converted to boolean
1 == True # will be true
'' == False # will be true

# all non-empty value will be true
# all empty or zero-equal value will be false





# integers
# http://web.cecs.pdx.edu/~harry/compilers/ASCIIChart.pdf

newInteger = 1

newInteger == 2

newInteger.__eq__(2)

type(newInteger)

print(newInteger)

1 == newInteger

1 is newInteger  # this is the same object!!

int_a = 5
int_a.__add__(4)
int_a + 4

print(5 > 3, 5 < 3, 5 * 3, 5 / 3)  # last expression returns the float value

5 // 2  # whole division

5 % 2  # modulo of division

print(int(5), int(5.3), int('5'))  # convert to int

# Python arithmetic operators
# + Addition	Adds values on either side of the operator.	a + b = 30
# - Subtraction	Subtracts right hand operand from left hand operand.	a – b = -10
# * Multiplication	Multiplies values on either side of the operator	a * b = 200
# / Division	Divides left hand operand by right hand operand	b / a = 2
# % Modulus	Divides left hand operand by right hand operand and returns remainder	b % a = 0
# ** Exponent	Performs exponential (power) calculation on operators	a**b =10 to the power 20
# //	Floor Division - removes the floating-point part of the result 5 //2 == 2

# Python Comparison Operators
# These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
#
# Assume variable a holds 10 and variable b holds 20, then −

# Operator	Description	Example
# ==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
# <>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
# >	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
# >=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.


# =	Assigns values from right side operands to left side operand	c = a + b assigns value of a + b into c
# += Add AND	It adds right operand to the left operand and assign the result to left operand	c += a is equivalent to c = c + a
# -= Subtract AND	It subtracts right operand from the left operand and assign the result to left operand	c -= a is equivalent to c = c - a
# *= Multiply AND	It multiplies right operand with the left operand and assign the result to left operand	c *= a is equivalent to c = c * a
# /= Divide AND	It divides left operand with the right operand and assign the result to left operand	c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
# %= Modulus AND	It takes modulus using two operands and assign the result to left operand	c %= a is equivalent to c = c % a
# **= Exponent AND	Performs exponential (power) calculation on operators and assign value to the left operand	c **= a is equivalent to c = c ** a
# //= Floor Division	It performs floor division on operators and assign value to the left operand	c //= a is equivalent to c = c // a

###### strings
a = 'string'

a == "string" == '''string''' == """string"""

multiline_string = '''
1st line
2nd line
'''

'string with spaces'.split()
a.startswith('s')
a.upper() == a
a * 2
a.capitalize()
a.capitalize == a.capitalize()
"conca" + 'tenation'  # operator + calls str.__add__ method under the hood

####### Some string methods
# Method	Description
# Python String capitalize()	Converts first character to Capital Letter
# Python String center()	Pads string with specified character
# Python String casefold()	converts to casefolded strings
# Python String count()	returns occurrences of substring in string
# Python String endswith()	Checks if String Ends with the Specified Suffix
# Python String expandtabs()	Replaces Tab character With Spaces
# Python String encode()	returns encoded string of given string
# Python String find()	Returns the index of first occurrence of substring
# Python String format()	formats string into nicer output
# Python String index()	Returns Index of Substring
# Python String isalnum()	Checks Alphanumeric Character
# Python String isalpha()	Checks if All Characters are Alphabets
# Python String isdecimal()	Checks Decimal Characters
# Python String isdigit()	Checks Digit Characters
# Python String isidentifier()	Checks for Valid Identifier
# Python String islower()	Checks if all Alphabets in a String are Lowercase
# Python String isnumeric()	Checks Numeric Characters
# Python String isprintable()	Checks Printable Character
# Python String isspace()	Checks Whitespace Characters
# Python String istitle()	Checks for Titlecased String
# Python String isupper()	returns if all characters are uppercase characters
# Python String join()	Returns a Concatenated String
# Python String ljust()	returns left-justified string of given width
# Python String rjust()	returns right-justified string of given width
# Python String lower()	returns lowercased string
# Python String upper()	returns uppercased string
# Python String swapcase()	swap uppercase characters to lowercase; vice versa
# Python String lstrip()	Removes Leading Characters
# Python String rstrip()	Removes Trailing Characters
# Python String strip()	Removes Both Leading and Trailing Characters
# Python String partition()	Returns a Tuple
# Python String maketrans()	returns a translation table
# Python String rpartition()	Returns a Tuple
# Python String translate()	returns mapped charactered string
# Python String replace()	Replaces Substring Inside
# Python String rfind()	Returns the Highest Index of Substring
# Python String rindex()	Returns Highest Index of Substring
# Python String split()	Splits String from Left
# Python String rsplit()	Splits String From Right
# Python String splitlines()	Splits String at Line Boundaries
# Python String startswith()	Checks if String Starts with the Specified String
# Python String title()	Returns a Title Cased String



##### string formatting
"formatted {}".format('string')  # empty placeholder

"This {0} is also formatted {0}".format('string')  # positional placeholder

"{S} is formatted with named {P}".format(S='string', P='placeholder')

var1 = 'string'
f'f-{var1} can use variable name as a placeholder'


# String length
len(var1)


##### string slices
a = 'abcdefg'

print(a[0], a[0:2], a[:2], a[:], a[::-1])  # five new objects created

print(a[:2])


### in operator to check affiliation of a symbol to a string
'a' in 'abc'
'd' in 'abc'
'f' not in 'abc'