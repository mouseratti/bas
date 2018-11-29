l1 = [5,9,8,90,64,55,89]

l1.sort()

#if __name__=__main__:
#	print(__name__)

def dictGenerate(firstKey=0,*list1):
	DICT = {}

	for oo in list1:
		l3={str(firstKey):oo}
		DICT.update(l3)
		firstKey+=1
	
	showDict(**DICT)


def showDict(**ee):
	for index,value in ee.items():
		print(index,' : ',value)

dictGenerate(0,*l1)


