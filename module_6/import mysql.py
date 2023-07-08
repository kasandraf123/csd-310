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





    insert_query_team = (
    "INSERT INTO team (id, name)"
    "VALUES (%s, %s)"
    )

    insert_query_player = (
    "INSERT INTO player (first_name, last_name, team_id)"
    "VALUES (%s, %s, %s)"
    )

    delete_query_player = (
        "DELETE FROM player WHERE first_name = %s AND last_name = %s"
    )

    update_team_query_of_player = (
    "UPDATE player SET team_id = %s WHERE first_name = %s AND last_name = %s"
    )

    def displayData():
        show_query = (
            "SELECT p.id, p.first_name, p.last_name, t.name "
            "FROM player p "
            "INNER JOIN team t on t.id = p.team_id"
        )
    cursor.execute(show_query)
    result = cursor.fetchall()
    for row in result:
        print("Player ID: {}".format(row[0]))
        print("First Name: {}".format(row[1]))
        print("Last Name: {}".format(row[2]))
        print("Team Name: {}".format(row[3]))
        print()

    # initial data
    cursor.execute(insert_query_team, [1, 'Team Gandalf'])
    cursor.execute(insert_query_team, [2, 'Team Sauron'])
    cursor.execute(insert_query_player, ['Thorin', 'Oakenshield', 1])
    cursor.execute(insert_query_player, ['Bilbo', 'Baggins', 1])
    cursor.execute(insert_query_player, ['Saruman', 'The White', 2])
    mydb.commit()

    # insert a new record into the player table for Team Gandalf. team_id = 1
    cursor.execute(insert_query_player, ['Frodo', 'Baggins', 1])
    mydb.commit()
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    displayData()

    # update the newly inserted record by changing the player's team to Team Sauron.
    cursor.execute(update_team_query_of_player, [2, 'Frodo', 'Baggins'])
    mydb.commit()
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    displayData()

    # execute a delete query to remove the updated record
    cursor.execute(delete_query_player, ['Frodo', 'Baggins'])
    mydb.commit()
    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    #displayData()