import os
import pymysql

#Get username from Cloud9 workspace
#(modify this variable if running on another device)
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #Run a querry
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()