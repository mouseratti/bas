from variables import a, b
print("Hello, BAS!")

TEXT = """
Add {} * {} / 2
Total {}.
"""

total = (a*b)/2


print(TEXT.format(a, b, total))

