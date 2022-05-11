import psycopg2

try:
    connect = psycopg2.connect(database='postgres',
                               user='postgres',
                               password='admin',
                               host='localhost',
                               port='6543')

    print('database created')
    cur = connect.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    cur.execute('''CREATE TABLE employee
                    (ID INT PRIMARY KEY NOT NULL,
                    NAME        TEXT    ,
                    ADDRESS     CHAR(50) NOT NULL,
                    SALARY      INT)''')

    insert_script = 'INSERT INTO employee (id, name, address, salary) VALUES (%s, %s, %s, %s)'
    insert_values = [(1, 'Teja', 'Hyd', 20000), (2, 'Sai', 'Bnglre', 22000), (3, 'Vamshi', 'Wrngl', 24000), (4, 'Kumar', 'Hyd', 23000), (5, 'Stephen', 'Rjmry', 22000)]
    for record in insert_values:
        cur.execute(insert_script, record)
        print(record)

    update_script = 'UPDATE employee SET salary = salary + (salary * 0.1)'
    cur.execute(update_script)
    print('Total no of rows Updated: ', cur.rowcount)
    print()

    delete_script = 'DELETE from employee WHERE id = 5'
    cur.execute(delete_script)
    print('Total No. of rows Deleted:', cur.rowcount)

    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print('Id = ', row[0])
        print('Name = ', row[1])
        print('Address = ', row[2])
        print('Salary = ', row[3], '\n')

except Exception as error:
    print(error)

finally:
    if connect:
        connect.commit()
        connect.close()
        print('Connection Closed')
