from variables import NUM1, NUM2
print("Hello, JOB2!")

TEXT = """
NUM1 = {}. NUM2 = {}  
"""

if NUM1 > NUM2:
	print ("NUM1 bolshe NUM2")
else:
	print ("NUM2 bolshe NUM1")



print(TEXT.format(NUM1, NUM2))