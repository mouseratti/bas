import sqlite3,time

datetime=time.clock()
query = """INSERT INTO bombaTable (userid,title,body,date) VALUES (?,?,?,?)"""

def dbInsert(*l1):
    conn = sqlite3.connect("/home/bas/bombaDB")

    if conn:
        print('Connection succes', conn)
        cursor = conn.cursor()

        for oo in range(0,len(l1)):
            cursor.execute(query, (l1[oo]['userId'], l1[oo]['title'], l1[oo]['body'], datetime))

        conn.commit()

    conn.close()

def dbUpdate(id):
    conn = sqlite3.connect("/home/bas/bombaDB")
    query = """UPDATE bombaTable SET userid=5,title='abas',body='eeeeee' where id=?"""

    if conn:
        print('Connection succes', conn)
        cursor = conn.cursor()

        cursor.execute(query, (id,))

        conn.commit()

    conn.close()