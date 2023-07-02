import mysql.connector
from mysql.connector import errorcode

config = {'host':'127.0.0.1',
          'database':'pysports',
         'user':'root',
          'password':'@Kf122397141159',
          'auth_plugin':'mysql_native_password'}

try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")


#print(connection)


#    if connection.is_connected():
#        db_info = connection.get_server_info()
#        print("Connected to MySQL Server version ", db_info)
#        cursor = connection.cursor()
#        cursor.execute("Select database();")
#        record = cursor.fetchbone()
#        print("You're connected to database: ", record)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


    
    
    #print("Error while connecting to MySQL", e)
finally:
    db.close()
    #if connection.is_connected():
    #    cursor.close()
    #    connection.close()
    #    print("MySQL connection is closed")
