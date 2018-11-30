import sqlite3
import time
import requests

DB = "my_base"
URL = "https://jsonplaceholder.typicode.com/posts"
QUERY = 'INSERT INTO posts (id, userId, title, body, created) VALUES (?,?,?,?,?)'
query2 = 'update posts set title = "bas", body = "python course" where id = 99 '
if __name__ == '__main__':
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    response = requests.get(URL)
    if response.ok:
        data = response.json()
        for x in data:
            cursor.execute(QUERY, (x.get('id'), x.get('userId'), x.get('title'), x.get('body'), time.time()))
        cursor.execute(query2)
    else:
        print("Bad response code: {}".format(response.status_code))
    conn.commit()
