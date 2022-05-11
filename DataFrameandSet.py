import pandas as pd
import psycopg2

class Employeedb:
    def connect(self):
        try:
            self.Connection = psycopg2.connect(database='postgres',
                                               user='postgres',
                                               password='admin',
                                               host='localhost',
                                               port='6543')
            print('Database Connected')
            self.cursor = self.Connection.cursor()
        except(Exception, psycopg2.Error) as error:
            print('Error while Connecting to postgreSQL', error)

    def CreateEmployeetb(self):
        self.cursor.execute('DROP TABLE IF EXISTS EMPLOYEEDB')
        self.cursor.execute('''CREATE TABLE Employeedb''')
        self.cursor.execute('SELECT * FROM Employeedb')

    def Data(self):
        self.d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
        self.df = pd.DataFrame(self.d)
        print(self.df)
        self.Connection.commit()

if __name__ == '__main__':
    db = Employeedb()
    db.connect()
    db.Data()
