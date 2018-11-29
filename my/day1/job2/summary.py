from variables import KAT1, KAT2
print("Hello, JOB2!")

TEXT = """
KAT1 = {}. KAT2 = {} . Ploshady = {} 
"""

PL = (KAT1 * KAT2) / 2 


print(TEXT.format(KAT1, KAT2, PL))