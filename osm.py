import sqlite3

db = sqlie3.connect('nodesnways')

def CountUsers():
    conn = connect()
    cur = conn.cursor()
    query = 'SELECT count(user) as TOT_Users FROM ways'
    cur.execute(query)
    conn.commit()
    conn.close()



