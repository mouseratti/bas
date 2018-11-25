from variables import NAME, AGE, POSITION
print("Hello, BAS!")

TEXT = """
My name is {}. I'm {} years old. It's about {} days.
My position is {}.
"""

age_days = 365.0 * AGE 


print(TEXT.format(NAME, AGE, age_days, POSITION))

