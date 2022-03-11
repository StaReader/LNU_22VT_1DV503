# This file handle all data insertion.

import mysql.connector
from mysql.connector import errorcode
from numpy import NaN
import pandas as pd

# Insert users data
def insert_users_data(cursor, cnx):
    data = pd.read_csv(r'users.csv', delimiter=',').fillna('0')
    data = data.values.tolist()
    for row in data:
        try:
            cursor.execute("INSERT INTO users ("
                           "user_name,"
                           "first_name,"
                           "last_name,"
                           "phone_number,"
                           "e_mail,"
                           "pin)"
                           "VALUES (%s,%s,%s,%s,%s,%s);",
                           (row[0], row[1], row[2], row[3], row[4], row[5]))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

# Insert games data
def insert_games_data(cursor, cnx):
    data = pd.read_csv(r'games.csv', delimiter=',')
    data = data.values.tolist()
    for row in data:
        try:
            cursor.execute("INSERT INTO games ("
                           "title,"
                           "release_date,"
                           "developer,"
                           "publisher)"
                           "VALUES (%s,%s,%s,%s);",
                           (row[0], row[1], row[2], row[3]))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

# Insert review data
def insert_review_data(cursor, cnx):
    data = pd.read_csv(r'reviews.csv', delimiter=',')
    data = data.values.tolist()
    for row in data:
        try:
            cursor.execute("INSERT INTO reviews ("
                           "game,"
                           "user,"
                           "content,"
                           "rating,"
                           "date)"
                           "VALUES (%s,%s,%s,%s,%s);",
                           (row[0], row[1], row[2], row[3], row[4]))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

# Insert model data
def insert_types_data(cursor, cnx):
    data = pd.read_csv(r'types.csv', delimiter=',')
    data = data.values.tolist()
    for row in data:
        try:
            cursor.execute("INSERT INTO types ("
                            "game,"
                            "genre)"
                            "VALUES (%s,%s);",
                            (row[0], row[1]))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

# Insert categorys data
def insert_genres_data(cursor, cnx):
    data = pd.read_csv(r'genres.csv', delimiter=',')
    data = data.values.tolist()
    for row in data:
        try:
            cursor.execute("INSERT INTO genres ("
                           "name)"
                           "VALUES (%s);",
                           (row[0],))
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()
