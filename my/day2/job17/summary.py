from variables import TEXT,FILE
import operator

D ={}


def CreateDictionary(word,textSplit):
	UI=0
	U = dict()
	global D
	for wordInB in textSplit:
		if wordInB==word:
			UI +=1	
			U={word:UI}	
			D.update(U)
	#print(U)

def fileWrite(filename,text):
	f = open(filename,'r+')
	f.truncate(0)
	f.write(str(text))
	f.close()

def fileRead(filename):
	f = open(filename,'r')
	stro =f.read(1000)
	textSplit = stro.split()
	uniqueWord = set(textSplit)
	f.close()
	for word1 in uniqueWord:
		CreateDictionary(word1,textSplit)



fileWrite(FILE,TEXT)
fileRead(FILE)	



def jkl(**aa):
	e=sorted(aa.items(),key=lambda x:x[1], reverse=True)
	print(e)


jkl(**D)



#for letter, number in D.items():
#	if number>10:
#		pass
#		print('Slovo ',letter,' vstre4aetsya ',number,' raz')

