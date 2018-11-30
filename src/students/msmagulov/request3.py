import urllib3
import sqlite3
import time
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
QUERY = '''
insert into post
(userId,title,body,date) values
(?,?,?,?)
'''
QUERY2 = '''
update post set title = 'bas', body = 'python course' where id=99
'''

if __name__ == '__main__':

    response = requests.get(url)
    if response.ok:

        jsoned = response.text
        data = json.loads(jsoned)
    conn = sqlite3.connect("/home/bas/PycharmProjects/bas/src/students/msmagulov/posts")
    cursor = conn.cursor()
    for post in data:
        cursor.execute(QUERY, (post.get('userId', 1), post['title'], post['body'], time.time()))
    conn.commit()
    cursor = conn.cursor()
    cursor.execute(QUERY2)
    conn.commit()
    assert data == response.json()
    print("response code: {}".format(response.status_code))

