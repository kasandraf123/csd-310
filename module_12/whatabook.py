import mysql.connector
from mysql.connector import errorcode


#CONNECT TO pysports database

config = {'host':'127.0.0.1',
          'database':'whatabook',
         'user':'root',
          'password':'@Kf122397141159',
          'auth_plugin':'mysql_native_password'}


def show_menu():
    print("\n  -- Main Menu --\n")
    print("Select one of the following:\n 1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      Please choose 1, 2, 3, or 4: '))

        return choice
    except ValueError:
        print("\n  Invaid input, ending program...\n")

        sys.exit(0)



def show_books(_cursor):
    query = "SELECT book_id, book_name, details, author from book"
    _cursor.execute(query)
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))



def show_locations(_cursor):
    query = "SELECT store_id, locate from store"
    _cursor.execute(query)
    
    show_locations = _cursor.fetchall()

    print("\n  -- DISPLAYING Location --")
    
    # iterate over locations
    for location in show_locations:
        print("  Store Id: {}\n Locate: {}\n".format(location[0], location[1]))


def validate_user():
    """ validate the users ID """

    try:
        user_id = int(input('\n      Enter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)


def show_account_menu():
    """ display the users account menu """

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    query = "SELECT book_id, book_name, author, details " + "FROM book " + "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id)

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))



def add_book_to_wishlist(_cursor, _user_id, _book_id):
     _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


    


def connect_database():
    db = mysql.connector.connect(**config)
    return db
    

def main():
    try:
        # Try/catch block for handling potential MySQL database errors
        db = connect_database()  # Connect to the WhatABook database
        cursor = db.cursor()  # Cursor for MySQL queries

        print("\nWelcome to the WhatABook Application!")

        while True:
            user_selection = show_menu()  # Show the main menu

            if user_selection == 1:
                show_books(cursor)
            elif user_selection == 2:
                show_locations(cursor)
            elif user_selection == 3:
                user_id = validate_user()
                while True:
                    account_option = show_account_menu()  # Show the account settings menu
                    if account_option == 1:
                        show_wishlist(cursor, user_id)
                    elif account_option == 2:
                        show_books_to_add(cursor, user_id)
                        book_id = int(input("\nEnter the id of the book you want to add: "))
                        add_book_to_wishlist(cursor, user_id, book_id)
                        db.commit()  # Commit the changes to the database
                        print("\nBook id: {} was added to your wishlist!".format(book_id))
                    elif account_option == 3:
                        break
                    else:
                        print("\nInvalid option, please retry...")
            elif user_selection == 4:
                print("\nProgram terminated...")
                break
            else:
                print("\nInvalid option, please retry...")

    except mysql.connector.Error as err:
        # Handle database errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password is invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)

    finally:
        cursor.close()
        db.close()  # Close the connection to MySQL
        input("\n\n  Press any key to continue...")

if __name__ == "__main__":
    main()
