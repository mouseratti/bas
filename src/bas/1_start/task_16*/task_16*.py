a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
res = []
for x in a1:
	for y in a2:
		if x in y:
			res.append(x)
			break
res.sort()
print(res)
