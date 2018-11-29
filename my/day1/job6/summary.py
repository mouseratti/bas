from variables import NUM1, NUM2, NUM3, NUM4, MASSIVE
print("Hello, JOB2!")

TEXT = """
NUM1 = {}. NUM2 = {}. NUM3 = {}. NUM4 = {}      
"""

TEXT2 = """
NUM1 = {}. NUM2 = {}. NUM3 = {}. NUM4 = {}. MIN = {}. MAX = {}.
"""

if NUM1 > NUM2 or NUM1 > NUM3  or NUM1 > NUM4 :
	print ("NUM1 bolshe VSEH")
elif NUM2 > NUM1 or NUM2 > NUM3  or NUM2 > NUM4 :
	print ("NUM2 bolshe VSEH")
elif NUM3 > NUM1 or NUM3 > NUM2  or NUM3 > NUM4 :
	print ("NUM3 bolshe VSEH")
elif NUM4 > NUM1 or NUM4 > NUM2  or NUM4 > NUM3 :
	print ("NUM4 bolshe VSEH")


SORT_MASSIVE= sorted(MASSIVE)

print (TEXT2.format(MASSIVE[0], MASSIVE[1], MASSIVE[2], MASSIVE[3], SORT_MASSIVE[0], SORT_MASSIVE[3]))




print(TEXT.format(NUM1, NUM2, NUM3, NUM4))