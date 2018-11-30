import requests,json,re
from sqlite import dbInsert,dbUpdate

url='https://jsonplaceholder.typicode.com/posts'
file='tt.txt'
myNote={'userId': 200, 'id': '', 'title': 'esd asd  glreg, opkg rmeigoer rpgm iore'}
e=list()

rof=open(file,'w+')
rof.truncate(0)

#ro = requests.post(url, data=myNote)
#print('request post = ', ro.status_code)

r = requests.get(url)
a=r.json()
for op in a:
    if re.search('\'id\': 101',str(op)):
        print(op)

#dbInsert(*a)

dbUpdate('199')


#print('responce is ',r)