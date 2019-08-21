'''
What is a set in Python?
A set is an unordered collection of items.
Every element is unique (no duplicates) and
must be immutable (which cannot be changed).
The set itself is mutable.
We can add or remove items from it.
Sets can be used to perform mathematical set operations like union,
intersection, symmetric difference etc.
'''
# creating a set
mySet = {1, 2, 3}

# creating an empty set
my_empty_set = set()



# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

print(mySet[0])

# add an element
# Output: {1, 2, 3}
mySet.add(2)
print(mySet)
# add multiple elements
# Output: {1, 2, 3, 4}
mySet.update([2, 3, 4])
print(mySet)
# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
mySet.update([4, 5], {1, 6, 8}, (1,2,8,5))
print(mySet)

# set operations
set1 = {'foo', 'bar', 'baz'}
set2 = {'baz', 'qux', 'quux'}
print(set1.union(set2))
print(set1.intersection(set2))
set1.intersection_update(set2)
set1 | set2
set1 - set2
set1 ^ set2
set1 & set2
