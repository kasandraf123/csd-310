import mysql.connector
from mysql.connector import errorcode


#CONNECT TO pysports database

config = {'host':'127.0.0.1',
          'database':'pysports',
         'user':'root',
          'password':'@Kf122397141159',
          'auth_plugin':'mysql_native_password'}

try:
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()

    query= "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    
    cursor.execute(query)
    rows=cursor.fetchall()
    
    print("\n-- DISPLAYING PLAYER RECORDS --")
    for x in rows:
        print("Player ID: {}".format(x[0]))
        print("First Name: {}".format(x[1]))
        print("Last Name: {}".format(x[2]))
        print("Team Name: {}\n".format(x[3]))
    

    cursor.close()
    db.close()

    input("\n\n  Press any key to continue...")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

    
finally:
    db.close()
