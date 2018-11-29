from collections import Counter
import re


FILE = 'log.log'

#pattern1=re.compile('^.*\"([A-Y]{3,9})')
pattern1=re.compile('^.*\"([A-Y]{3,9}).(.*\?|.*HTTP)')

def requestSearch(*l1):
    getNum = 0
    postNum = 0
    delNum = 0
    psttNum = 0
    l3=list()
    l4=list()
    lget=list()
    lput= list()
    ldel = list()

    for ll in l1:
        for ll2 in ll:
            if ll2[0] == 'GET':
                lget.append(ll2[1])
            if ll2[0] == 'PUT':
                lput.append(ll2[1])
            if ll2[0] == 'DELETE':
                ldel.append(ll2[1])
            l3.append(ll2[1])
            l4.append(ll2[0])

    print(" GET = ",l4.count('GET')," PUT = ",l4.count('PUT')," DELETE = ",l4.count('DELETE')," POST = ",l4.count('POST'))

    print(len(set(lput)))


    print(Counter(l3).most_common(3))
    print(' get = ',Counter(lget).most_common(3))
    print(' put = ',Counter(lput).most_common(3),' put = ',Counter(lput).most_common(3),' put = ',)
    print(' delete = ',Counter(ldel).most_common(3))


def fileDef(fileName):
    STRINNUM=list()

    FOPEN = open(fileName, 'r+')
    asd=list()

    for line in FOPEN.readlines():
        STRINNUM.append(line)
        asd.append(re.findall(pattern1,line))

    print('Vsego strok :', len(STRINNUM))

    requestSearch(*asd)

    FOPEN.close()


fileDef(FILE)


