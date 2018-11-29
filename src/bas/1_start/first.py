#!/usr/bin/env python3
from variables import *
print("Hello, BAS!")

TEXT: str = """
My name is {}. I'm {} years old. It's about {} days.
My position is {}.
"""
TEXT = None

age_days = 365.0 * AGE 


print(TEXT.format(NAME, AGE, age_days, POSITION))

