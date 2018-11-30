from task_1_var import A, B, C
TEXT = """
A = {}
B = {}
C = {}
A+B+C={}
"""
SUM = A + B + C
print(TEXT.format(A, B, C, SUM))