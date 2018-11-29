from variables import TEXT
import operator

textSplit = list(TEXT)

#print(textSplit)

def DictCreate(**vowels):
	print(vowels)


def WordFind(*arg):

	vowels = ['A','E','I','O','U']
	consonants = ['B','G','F','H']
	V = dict()
	C = dict()

	for ie in vowels:
		anum = 0
		for io in arg:
			if io.upper() == ie:
				anum += 1
		V.update({ie:anum})
	
	print(V)


	for ie in consonants:
		bnum = 0
		for ioo in arg:
			if ioo.upper() == ie:
				bnum += 1
		C.update({ie:anum})
	
	print(C)	
	DictCreate(**{'vowels':{**V},'consonants':{**C}})
	#print(arg)


	#print(dict((i, arg.count(i)) for i in arg))

WordFind(*textSplit)