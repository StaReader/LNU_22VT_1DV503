# Programming assignment 2

import mysql.connector
from mysql.connector import errorcode
import msvcrt as msc

from tables import *
from data import *
from queries import *

# Connect to phpMyAdmin
cnx = mysql.connector.connect(  user='root',
                                password='root',
                                host='localhost',
                                port='8889'
                             )

DATABASE = 'assignment2'
cursor = cnx.cursor()

# Create database
def create_database(cursor, db_name):
    try:
        cursor.execute( f"""
                        CREATE DATABASE {db_name}
                        DEFAULT CHARACTER SET 'utf8'
                         """)
    except mysql.connector.Error as err:
        print("Faild to create database {db_name}")
        exit(1)

# Connect to or create -database
try:
    cursor.execute(f'USE {DATABASE}')
except mysql.connector.Error as err:
    print(f"Database {DATABASE} does not exist.")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, DATABASE)
        print(f"Database {DATABASE} create succesfully.")
        cnx.database = DATABASE
        create_table_users(cursor)
        create_table_games(cursor)
        create_table_reviews(cursor)
        create_table_types(cursor)
        create_table_geners(cursor)
        insert_users_data(cursor, cnx)
        insert_games_data(cursor, cnx)
        insert_review_data(cursor, cnx)
        insert_types_data(cursor, cnx)
        insert_genres_data(cursor, cnx)
        create_view_users(cursor)
    else:
        print(err)

# Menu
choose = 10
while choose != 0:
    try:
        # Print menu
        print('\n'*10)
        print('MENU\n')
        print('1.  List all users.')
        print('2.  List all games.')
        print('3.  Search for user information.')
        print('4.  Search for reviews for a game.')
        print('5.  Top 10 rated games.')
        print('6.  Top 10 active users.')
        print('7   Most used genre for game development.')
        print('0.  End Program.')

        # User choose from menu.
        choose = eval(input('\nEnter: '))
        if(choose == 1):
            print_users(cursor)
            msc.getch()
        elif(choose == 2):
            print_all_games(cursor)   
            msc.getch()
        elif(choose == 3):
            print_user_info(cursor)
            msc.getch()
        elif(choose == 4):
            print_reviews(cursor)
            msc.getch()
        elif(choose == 5):
            get_top_games(cursor)
            msc.getch()
        elif(choose == 6):
            get_top_users(cursor)
            msc.getch()
        elif(choose == 7):
            get_first_genre(cursor)
            msc.getch()
    except:
        print('')

cursor.close()
cnx.close()