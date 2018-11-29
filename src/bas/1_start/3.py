from variables import *
print("Hello, BAS!")

TEXT: str = """
Number1 = {},Number2 = {}
Sorted min = {}.
"""

# c = c.sort([a,b])

num = [a,b,c,d,e,f,g]
num2 = []

while num:
	minimum = num[0]
  for x in num:
  	if x < minimum:
  		minimum = x
  num2.append(minimum)
  num.remove(minimum)
print num2

