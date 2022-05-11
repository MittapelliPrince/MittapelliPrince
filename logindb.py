import psycopg2


conn = psycopg2.connect(user='postgres', database='postgres', password='admin', host='localhost', port='6543')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS login_db')
cursor.execute("""CREATE TABLE login_db
                (username   TEXT    NOT NULL,
                 password   varchar NOT NULL)""")
insert_query = 'INSERT INTO login_db(username, password) VALUES(%s, %s)'
insert_values = [('Prince', 159753), ('Suman', 852456)]
for record in insert_values:
    cursor.execute(insert_query, record)

conn.commit()
print('database created')
conn.close()