########################################################################################################################
import time
import psycopg2
import pandas as pd
from PyQt5.QtCore import QDateTime, QTime, Qt, QDate
import datetime
import json
import numpy as np

########################################################################################################################

class TargetDatabaseClient():
    try:
        with open('Configuration/FTP_IP_Config.json', 'r') as myfile:
            data = myfile.read()
        ServerConfigDict = json.loads(data)  # convert string to dict ###
    except:
        HS_dict = {
            'FTP_IP_Addrs': 'localhost',
            'FTP_username': '',
            'FTP_password': '',
            'DB_Host': 'localhost',
            'DB_Port': '6543',
            'Database': 'postgres',
            'DB_username': 'postgres'
        }
        with open('Configuration/FTP_IP_Config.json', 'w') as json_file:
            json.dump(HS_dict, json_file)

        with open('Configuration/FTP_IP_Config.json', 'r') as myfile:
            data = myfile.read()
        ServerConfigDict = json.loads(data)
    #  print(SensorInfoDict)
    DB_Host = ServerConfigDict['DB_Host']
    DB_Port = ServerConfigDict['DB_Port']
    Database = ServerConfigDict['Database']
    DB_username = ServerConfigDict['DB_username']
    DB_Password = 'Platinum0435#'

    def __init__(self, host=DB_Host, port=DB_Port, database=Database, user=DB_username, password=DB_Password):
        self.host = host
        self.port = str(port)
        self.database = database
        self.user = user
        self.password = password
        self.connection = 0
        self.CurDbTable = None

    ####################################################################################################################
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
        # print('***************  Connection Established  *****************')
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################
    def CreateIntReqDatabaseTable(self):
        try:
            cursor = self.connection.cursor()
            #  delete_table_query = f'''DROP TABLE IF EXISTS TemperatureEvent;'''
            #  cursor.execute(delete_table_query)
            #  self.connection.commit()
            create_table_query = f'''CREATE TABLE IF NOT EXISTS IntReqDatabase
                                             (date         TEXT NOT NULL,
                                             time     TEXT NOT NULL,
                                             requesting_terminal         TEXT NOT NULL,                                             
                                             easting      INT,
                                             northing      INT,
                                             height     INT,
                                             gen_loc     TEXT NOT NULL,
                                             info_question    TEXT NOT NULL,
                                             remarks     TEXT NOT NULL,
                                             resource_allocation    TEXT NOT NULL,
                                             assessment_from_disc    TEXT NOT NULL
                                             ); '''
            cursor.execute(create_table_query)
            self.connection.commit()
            # print("Table created successfully in PostgreSQL ")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)

    ####################################################################################################################
    def InsertIntoIntReqDatabaseTable(self, HS_dict):
        try:
            cursor = self.connection.cursor()
            print(HS_dict)
            insert_table_query = f'''INSERT INTO IntReqDatabase VALUES('{HS_dict['date']}','{HS_dict['time']}','{HS_dict['requesting_terminal']}','{HS_dict['easting']}','{HS_dict['northing']}','{HS_dict['height']}','{HS_dict['gen_loc']}','{HS_dict['info_question']}','{HS_dict['remarks']}','{HS_dict['resource_allocation']}','{HS_dict['assessment_from_disc']}' '''
            insert_table_query = insert_table_query + ');'
            #print(insert_table_query)
            cursor.execute(insert_table_query)
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error in inserting to IPBDatabase Table ", error)

    ####################################################################################################################
    def UpdateIntReqDataBase(self, DataString=['Not Yet Processed', 'Not Yet Processed'],
                             MatchDataDist={}):
        try:
            cursor = self.connection.cursor()
            queryCMD = f'''UPDATE IntReqDatabase SET resource_allocation = '{DataString[0]}', assessment_from_disc =  '{DataString[1]}' WHERE requesting_terminal ='{MatchDataDist['requesting_terminal']}' AND date = '{MatchDataDist['date']}' AND time = '{MatchDataDist['time']}';'''
            cursor.execute(queryCMD)
            self.connection.commit()
        except:
            print('Error in Updating User_ManagementDB Table.')

    ####################################################################################################################
    def GetIntReqDatabaseTable(self):
        try:
            # querycmd=f'''select * from SETLevelTargetData WHERE date between '{startdate}' and '{enddate}' and {AccessLevel}='{username}' ;'''
            querycmd = f'''SELECT * FROM IntReqDatabase WHERE assessment_from_disc = 'Not Yet Processed' ;'''
            self.CurDbTable = pd.read_sql_query(querycmd, con=self.connection)
            return self.CurDbTable
        except:
            print('Error in reading IPBDatabase Table.')
            return None
    ####################################################################################################################

if __name__ == "__main__":
    tb = TargetDatabaseClient()
    tb.connect()
    if tb.connection:
        tb.CreateIntReqDatabaseTable()
########################################################################################################################