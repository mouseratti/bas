import re
string = 'str1'
pattern_string = "\w"
re.match(pattern_string,string)
re.search(pattern_string, string)
re.findall(pattern_string, string)
result = re.finditer(pattern_string, string)

for obj in result:
    print(obj)


p = re.compile(pattern_string)

p.findall(string)
"""
[1,2,3] - конкретные символы
{0, 9} - возможное количество символов (от 0 до 9)
? 
+
.*
"""