from variables import TEXT
import operator

textSplit = TEXT.split()
#print(textSplit)

uniqueWord = set(textSplit)
#print(A)
D ={}



def CreateDictionary(word):
	UI=0
	U = dict()
	global D
	for wordInB in textSplit:
		if wordInB==word:
			UI +=1	
			U={word:UI}	
			D.update(U)
	#print(U)

for word1 in uniqueWord:
	CreateDictionary(word1)

def jkl(**aa):
	e=sorted(aa.items(),key=lambda x:x[1], reverse=True)
	print(e[:4:])

jkl(**D)

#for letter, number in D.items():
#	if number>10:
#		pass
#		print('Slovo ',letter,' vstre4aetsya ',number,' raz')

