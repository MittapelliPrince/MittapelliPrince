import psycopg2


class Students:
    def connect(self):
        try:
            self.connection = psycopg2.connect(database='postgres',
                                               user='postgres',
                                               password='admin',
                                               host='localhost',
                                               port='6543')
            print('Database Connected')
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print('Error while Connecting to postgreSQL', error)

    def Create_table_db(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute('DROP TABLE IF EXISTS students')
            self.cursor.execute('''CREATE TABLE students
                                (ID     INT PRIMARY KEY,
                                 NAME   TEXT NOT NULL,
                                 ADDRESS CHAR(50),
                                 ROLLNO INT)''')
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error while Creating table', error)

    def Add_record_db(self):
        try:
            self.cursor = self.connection.cursor()
            self.Add_record = 'INSERT INTO students(id, name, address, rollno) VALUES (%s, %s, %s, %s)'
            self.Add_values = [(1, 'Ram', 'Hyd', 123456), (2, 'Kumar', 'Wrngl', 123789),
                               (3, 'Sharath', 'Chennai', 159753)]
            for record in self.Add_values:
                self.cursor.execute(self.Add_record, record)
                print(record)
            print()
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error in inserting to Students table', error)

    def Modify_record_db(self):
        try:
            self.cursor = self.connection.cursor()
            self.Modify_record = 'UPDATE students SET rollno=456123 WHERE id = 2'
            self.cursor.execute(self.Modify_record)
            print('Total No. of rows Updated: ', self.cursor.rowcount)
            self.cursor.execute('SELECT * FROM students')
            rows = self.cursor.fetchall()
            for row in rows:
                print('Id = ', row[0])
                print('Name = ', row[1])
                print('Address = ', row[2])
                print('Rollno = ', row[3], '\n')
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error in Modifying record in students table', error)

    def Delete_record_db(self):
        try:
            self.cursor = self.connection.cursor()
            self.delete_record = 'DELETE FROM students WHERE id = 3'
            self.cursor.execute(self.delete_record)
            print('Total No. of rows Deleted: ', self.cursor.rowcount)
            self.cursor.execute('SELECT * FROM students')
            rows = self.cursor.fetchall()
            for row in rows:
                print('Id = ', row[0])
                print('Name = ', row[1])
                print('Address = ', row[2])
                print('Rollno = ', row[3], '\n')
            self.connection.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print('Error in Deleting record in Students table', error)

    def Connection(self):
        self.connection.commit()
        self.connection.close()
        print('Connection Closed')


if __name__ == '__main__':
    students = Students()
    students.connect()
    if students.connection:
        students.Create_table_db()
        students.Add_record_db()
        students.Modify_record_db()
        students.Delete_record_db()
        students.Connection()
