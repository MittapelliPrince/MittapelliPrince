import psycopg2


class students():
    def __init__(self):
        super().__init__()
        self.connect = psycopg2.connect(database='postgres',
                                   user='postgres',
                                   password='admin',
                                   host='localhost',
                                   port='6543')
        print('Database Connected')
        self.cur = self.connect.cursor()
        self.Create_table_db()
        self.Add_record_db()
        self.Modify_record_db()
        self.Delete_record_db()
        self.Delete_db()

    def Create_table_db(self):
        self.cur.execute('DROP TABLE IF EXISTS students')
        self.cur.execute('''CREATE TABLE students
                            (ID     INT PRIMARY KEY,
                             NAME   TEXT NOT NULL,
                             ADDRESS CHAR(50),
                             ROLLNO INT)''')

    def Add_record_db(self):
        self.insert_script = 'INSERT INTO students(id, name, address, rollno) VALUES (%s, %s, %s, %s)'
        self.insert_values = [(1, 'Ram', 'Hyd', 123456), (2, 'Kumar', 'Wrngl', 123789), (3, 'Sharath', 'Chennai', 159753)]
        for record in self.insert_values:
            self.cur.execute(self.insert_script, record)
            print(record)
        print()

    def Modify_record_db(self):
        self.update_script = 'UPDATE students SET rollno=456123 WHERE id = 2'
        self.cur.execute(self.update_script)
        print('Total No. of rows Updated: ', self.cur.rowcount)
        self.cur.execute('SELECT * FROM students')
        rows = self.cur.fetchall()
        for row in rows:
            print('Id = ', row[0])
            print('Name = ', row[1])
            print('Address = ', row[2])
            print('Rollno = ', row[3], '\n')

    def Delete_record_db(self):
        self.delete_script = 'DELETE FROM students WHERE id = 3'
        self.cur.execute(self.delete_script)
        print('Total No. of rows Deleted: ', self.cur.rowcount)
        self.cur.execute('SELECT * FROM students')
        rows = self.cur.fetchall()
        for row in rows:
            print('Id = ', row[0])
            print('Name = ', row[1])
            print('Address = ', row[2])
            print('Rollno = ', row[3], '\n')

    def Delete_db(self):
        self.delete_db = 'DELETE FROM students'
        self.cur.execute(self.delete_db)
        print('Total No. of rows Deleted: ', self.cur.rowcount)
        
    def Connection(self):
        print('Connection Closed')
        self.connect.commit()
        self.connect.close()

class main():
    students = students()
