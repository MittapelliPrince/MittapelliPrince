import psycopg2


connect = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost', port='6543')

print('Database Created')
cur = connect.cursor()

cur.execute('UPDATE Employee set name = sai WHERE id = 4')

print('Total No. of rows Updated: ', cur.rowcount)

cur.execute('SELECT * from Employee')
rows = cur.fetchall()
for row in rows:
    print('ID = ', row[0])
    print('NAME = ', row[1])
    print('ADDRESS = ', row[2])
    print('SALARY = ', row[3], '\n')

print('Updated Successfully')
connect.commit()
connect.close()
