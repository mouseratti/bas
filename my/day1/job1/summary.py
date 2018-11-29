from variables import NUM1, NUM2, NUM3
print("Hello, JOB1!")

TEXT = """
First {}. Second {} . Third {} .
Summ is {}.
"""

SUMM = NUM1 + NUM2 + NUM3 


print(TEXT.format(NUM1, NUM2, NUM3, SUMM))