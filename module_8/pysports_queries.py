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
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    # EXECUTE SQL QUERIES FOR TEAM AND PLAYER TABLES

    cursor = db.cursor()

    team_query = "SELECT team_id, team_name, mascot FROM team"
    player_query = "SELECT player_id, first_name, last_name, team_id FROM player"

    cursor.execute(team_query)
    teams = cursor.fetchall()

    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Team Mascot: {}\n".format(team[2]))

 
    cursor.execute(player_query)
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}\n".format(player[3]))


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


