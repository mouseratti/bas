from variables import INT1, INT2, INT3
print("Hello, BAS!")

TEXT = """
Add {} + {} + {} 
Total {}.
"""

total = INT1 + INT2 + INT3 


print(TEXT.format(INT1, INT2, INT3, total))


