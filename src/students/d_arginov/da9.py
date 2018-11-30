import sqlite3
import time
import requests
import json

QWERY = '''
insert into posts 
(id, user_id, title, body, date) values 
(?, ?, ?, ?, ?)'''

if __name__ == '__main__':
    response = requests.get()
    if response.ok:

        jsoned = response.text
        data = json.loads(jsoned)
        for post in data:
            cursor.execute(QWERY, (post.get(3, 4, "data", "title", "body"))
        assert data == response.json()
    else:
        print("Bad response code: {}".format(response.status_code))

conn = sqlite3.connect("/home/bas/PycharmProjects/bas/src/students/d_arginov/dbda888")
cursor =  conn.cursor()
cursor.execute(QWERY,(3, 4, "data", "title", "body"))
conn.commit()
conn.close()

