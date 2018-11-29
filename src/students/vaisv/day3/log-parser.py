import re

FILE = 'log.log'

pattern1=re.compile('^.*\"([A-Y]{3,9})')


def requestSearch(*l1):
    getNum = 0
    postNum = 0
    delNum = 0

    for ll in l1:
        if ll == ['GET']:
            getNum += 1
        elif ll == ['PUT']:
            postNum += 1
        elif ll == ['DELETE']:
            delNum += 1

    print(" GET = ",getNum," PUT = ",postNum," DELETE = ",delNum)

def fileDef(fileName):

    FOPEN = open(fileName, 'r+')
    asd=list()

    STRINNUM = FOPEN.readlines()

    for line in STRINNUM:
        asd.append(re.findall(pattern1,line))

    print('Vsego strok :', len(STRINNUM))
    print ('Vsego HTTP metodov : ',set(asd))

    FOPEN.close()

    requestSearch(*asd)


fileDef(FILE)


