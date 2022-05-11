import psycopg2

class connect():
    def __init__(self):
        super().__init__()
        connect = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost', port='6543')

        print('Database Created')
        cur = connect.cursor()

        cur.execute('DELETE from Employee where ID = 2')

        print('Total No. of rows Deleted: ', cur.rowcount)

        cur.execute('SELECT * from Employee')
        rows = cur.fetchall()
        for row in rows:
            print('ID = ', row[0])
            print('NAME = ', row[1])
            print('ADDRESS = ', row[2])
            print('SALARY = ', row[3], '\n')

        print('Deleted Successfully')
        connect.commit()
        connect.close()

if __name__ == '__main__':
    connect = connect()