
import mysql.connector
from mysql.connector import errorcode

# User names
def print_users(cursor):
    cursor.execute( """
                    SELECT user_name
                    FROM users
                    """)
    print('\n'*20)
    print('User name')
    print('-'*15)
    for name in cursor:
        print(name[0])

# User information
def print_user_info(cursor):
    try:
        name = input('Enter user name: ')
        cursor.execute(f"""
                        SELECT first_name, last_name, phone_number, e_mail
                        FROM users
                        WHERE user_name = '{name}'
                        """)
        print('\n'*20)
        info = cursor.fetchone()
        if not info:
            print('No user with that name found.')
        else:
            print(f"{name} information:")
            print('-'*20)
            print(f"name : {info[0]} {info[1]}")
            print(f"email: {info[3]}")
            if info[2] == '0':
                print('phone: missing')
            else:
                print(f"phone: 0{info[2].strip('.0')}")
    except:
        print("Could not execute the query.")


# Print all games
def print_all_games(cursor):
    cursor.execute( """
                    SELECT title
                    FROM games
                    GROUP BY games.title
                    """)
    print('\n'*20)
    print('Game Title')
    print('-'*15)
    for title in cursor:
        print(title[0])

# Print reviews on given game
def print_reviews(cursor):
    try:
        game = input('Enter name of game: ')
        cursor.execute(f"""
                        SELECT reviews.content, reviews.date, reviews.rating, users.user_name
                        FROM reviews
                        INNER JOIN games 
                        ON reviews.game = games.game_id
                        INNER JOIN users
                        ON reviews.user = users.user_id
                        WHERE games.title = "{game}"
                        """)
        list = cursor.fetchall()
        print('\n'*20)
        print(f"\nReviews on {game}")
        print("-"*80)
        if not list:
            print('No review found.')
        else:
            for row in list:
                print(f"Author: {row[3]}{' '*56}{row[1]}\n")
                chunks = [row[0][i:i+80] for i in range(0, len(row[0]), 80)]
                for line in chunks:
                    print(line)
                print(f"\nRating: {row[2]}")
                print("-"*80)
    except:
        print("Could not execute the query.")


# Average rating of game
def get_games_rating(cursor):
    cursor.execute(f"""
                    SELECT ROUND(AVG(reviews.rating),2) AS av, games.title
                    FROM reviews
                    INNER JOIN games
                    ON reviews.game = games.game_id
                    GROUP BY games.title
                    ORDER BY av DESC
                    LIMIT 0, 10
                    """)
    print('\n'*20)
    print(f"{'Rating:':10s} Game Title")
    print('-'*30)
    for dec, title in cursor:
        print(f"{dec!s:11s}{title}")

#  Count the amount of reviews each user have written.
def get_user_reviews_count(cursor):
    cursor.execute(f"""
                    SELECT COUNT(reviews.user) AS cn, user_name
                    FROM reviews
                    INNER JOIN users
                    ON reviews.user = users.user_id
                    GROUP BY reviews.user
                    ORDER BY cn DESC
                    LIMIT 0, 10
                    """)
    print('\n'*20)
    print(f"{'Reviews:':10s} Name")
    print('-'*30)

    for num, name in cursor:
        print(f"{num!s:11s}{name}")

# Get the category that is mostly used in the games of the database
def get_max_category(cursor):
    cursor.execute(f"""
                    SELECT genres.name, COUNT(genres.name) AS cn
                    FROM genres
                    INNER JOIN types
                    ON genres.genre_id = types.genre
                    GROUP BY genres.name
                    ORDER BY cn DESC
                    LIMIT 0, 1
                    """)
    row = cursor.fetchone()
    print('\n'*20)
    print(f"The most used genre is {row[0]}, being the model for {row[1]} different games.")