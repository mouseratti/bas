import sqlite3
import time
QUERY = '''
insert into post
(userId,title,body,date) values
(?,?,?,?)
'''
conn = sqlite3.connect("/home/bas/PycharmProjects/bas/src/students/msmagulov/posts")
cursor = conn.cursor()
cursor.execute(QUERY,(1,'title2','body2',time.time()))
conn.commit()
