import psycopg2

try:
    connect = psycopg2.connect(database='postgres',
                               user='postgres',
                               password='admin',
                               host='localhost',
                               port='6543')

    print('Database Created')
    cur = connect.cursor()

    cur.execute('DROP TABLE IF EXISTS company ')
    create_table = '''CREATE TABLE company
                (ID     INT    PRIMARY KEY,
                 NAME   TEXT   NOT NULL,
                 ADDRESS CHAR(50),
                 SALARY INT)'''
    insert_script = 'INSERT INTO company(id, name, address, salary) VALUES (%s, %s, %s, %s)'
    insert_values = [(1, 'Teja', 'Hyd', 20000), (2, 'Sai', 'Bnglre', 22000), (3, 'Vamshi', 'Wrngl', 25000)]
    for record in insert_values:
        cur.execute(insert_script, record)

except Exception as error:
    print(error)
finally:
    print('Inserted Successfully')
    connect.commit()
    connect.close()
