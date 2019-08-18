a1 = ["strong", "arp", "live", ]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

result = set()

for elem1 in a1:
    for elem2 in a2:
        if elem1 in elem2:
            result.add(elem1)
result
print(result)

