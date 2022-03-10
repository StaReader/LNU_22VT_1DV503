# This file contains all tables creation.

import mysql.connector
from mysql.connector import errorcode

# Create table
def create_table(cursor, table):
    try:
        print('Creating table: ')
        cursor.execute(table)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('already exists.')
        else:
            print(err.msg)
    else:
        print('OK')

# Create users table
def create_table_users(cursor):
    users_querie = ("CREATE TABLE users ("
                    "user_id INT AUTO_INCREMENT,"
                    "user_name VARCHAR(20),"
                    "first_name VARCHAR(20),"
                    "last_name VARCHAR(20),"
                    "phone_number VARCHAR(20),"
                    "e_mail VARCHAR(30),"
                    "PRIMARY KEY(user_id))")

    create_table(cursor, users_querie)

# Create games table
def create_table_games(cursor):
    games_querie = ("CREATE TABLE games ("
                    "game_id INT AUTO_INCREMENT,"
                    "title VARCHAR(30),"
                    "release_date VARCHAR(20),"
                    "developer VARCHAR(100),"
                    "publisher VARCHAR(100),"
                    "PRIMARY KEY(game_id))")

    create_table(cursor, games_querie)

# Create reviews table
def create_table_reviews(cursor):
    reviews_querie = ("CREATE TABLE reviews ("
                      "review_id INT AUTO_INCREMENT,"
                      "game INT,"
                      "user INT,"
                      "content VARCHAR(500),"
                      "rating SMALLINT,"
                      "date VARCHAR(20),"
                      "PRIMARY KEY(review_id),"
                      "FOREIGN KEY(game) REFERENCES games(game_id),"
                      "FOREIGN KEY(user) REFERENCES users(user_id))")

    create_table(cursor, reviews_querie)

# Create model table
def create_table_types(cursor):
    model_querie = ("CREATE TABLE types ("
                    "game INT,"
                    "genre INT)")
    create_table(cursor, model_querie)

# Create categorys
def create_table_geners(cursor):
    genres_querie = ("CREATE TABLE genres ("
                       "genre_id INT AUTO_INCREMENT,"
                       "name VARCHAR(20),"
                       "PRIMARY KEY(genre_id))")
    create_table(cursor, genres_querie)
