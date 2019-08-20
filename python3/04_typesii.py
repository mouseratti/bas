# Python Lists
# The list is a most versatile datatype available in Python which can be written as a list
# of comma-separated values (items) between square brackets.
# Important thing about a list is that items in a list need not be of the same type.

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

l4 = [1,1,2,2,3,3] # elements may be repeated

empty_list = list()
list_from_string = list('string')


list1[0]
list2[2:3]
list_from_string[:] is list_from_string
list_from_string[::-1]


# List is a mutable structure - You can update single or multiple elements of lists
# by giving the slice on the left-hand side of the assignment operator,
# and you can add to elements
# in a list with the append() method.
list_from_string.append(2)
list_from_string.append('new element')


# Methods of list type
# 1	list.append(obj)
# Appends object obj to list
#
# 2	list.count(obj)
# Returns count of how many times obj occurs in list
#
# 3	list.extend(seq)
# Appends the contents of seq to list
#
# 4	list.index(obj)
# Returns the lowest index in list that obj appears
#
# 5	list.insert(index, obj)
# Inserts object obj into list at offset index
#
# 6	list.pop(obj=list[-1])
# Removes and returns last object or obj from list
#
# 7	list.remove(obj)
# Removes object obj from list
#
# 8	list.reverse()
# Reverses objects of list in place
#
# 9	list.sort([func])
# Sorts objects of list, use compare func if given


################ tuples
# May be considered as immutable version of list

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = 1,
tup5 = tuple()
tup6 = tuple(list_from_string)

# You can not change tuple after creation
tup6[1] = 2
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-129-8f19293459b0> in <module>
# ----> 1 tup6[1] = 2
#
# TypeError: 'tuple' object does not support item assignment



# Dicionaries
# Dictionary is a hashmap implementation in Python
# It stores values by their keys
# Empty dictionaries
d1 = {}
d2  = dict()

# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type,
# but the keys must be of an immutable data type such as strings, numbers, or tuples.
d3 = {
    'key1': 'value2',
    'k2': 'another string value',
    2: 3, 3: 3,
    (1,2,3): [4,5,6]
}


# To access dictionary elements, you can use the familiar square brackets along
# with the key to obtain its value
d3['key1']
d3['key2']
d3.get('key2')

# dictionary methods
# 1	dict.clear()
# Removes all elements of dictionary dict
#
# 2	dict.copy()
# Returns a shallow copy of dictionary dict
#
# 3	dict.fromkeys()
# Create a new dictionary with keys from seq and values set to value.
#
# 4	dict.get(key, default=None)
# For key key, returns value or default if key not in dictionary
#
# 5	dict.has_key(key)
# Returns true if key in dictionary dict, false otherwise
#
# 6	dict.items()
# Returns a list of dict's (key, value) tuple pairs
#
# 7	dict.keys()
# Returns list of dictionary dict's keys
#
# 8	dict.setdefault(key, default=None)
# Similar to get(), but will set dict[key]=default if key is not already in dict
#
# 9	dict.update(dict2)
# Adds dictionary dict2's key-values pairs to dict
#
# 10	dict.values()
# Returns list of dictionary dict's values
