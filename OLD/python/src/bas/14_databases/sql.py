import sqlite


DB = "/tmp/bas.db"


if __name__ == '__main__':
    conn = sqlite.connect(DB)
    cursor = conn.cursor
