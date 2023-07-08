import mysql.connector
from mysql.connector import errorcode


#CONNECT TO pysports database

config = {'host':'127.0.0.1',
          'database':'pysports',
         'user':'root',
          'password':'@Kf122397141159',
          'auth_plugin':'mysql_native_password'}

def show_players(cursor, title):

    try:
        db = mysql.connector.connect(**config)
    
        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        # EXECUTE SQL QUERIES FOR TEAM AND PLAYER TABLES

        cursor = db.cursor()
        # get the results from the cursor object 
        players = cursor.fetchall()

        print("\n  -- {} --".format(title))

        # iterate over the player data set and display the results 
        for player in players:
            print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
        # insert player query 
        add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                    "VALUES(%s, %s, %s)")

        # player data fields 
        player_data = ("Smeagol", "Shire Folk", 1)

        # insert a new player record
        cursor.execute(add_player, player_data)

        # commit the insert to the database 
        db.commit()

        # show all records in the player table 
        show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

        # update the newly inserted record 
        update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

        # execute the update query
        cursor.execute(update_player)

        # show all records in the player table 
        show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

        # delete query 
        delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

        cursor.execute(delete_player)


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


