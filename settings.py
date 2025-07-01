from dotenv import load_dotenv
import os
from pymongo import MongoClient
import datetime

load_dotenv() 


#Поиск фильмов My_SQL

DATABASE_MYSQL_R = {

    'host': os.getenv('MYSQL_HOST'),

    'user': os.getenv('MYSQL_USER'),

    'password': os.getenv('MYSQL_PASSWORD'),

    'charset': 'utf8mb4'

}

DATABASE_MYSQL_NAME = 'sakila'

COUNT_FILM = '''

    SELECT COUNT(film_id)

    FROM film

    '''

FILM_NAME_QUERY = """
    SELECT f.title, f.release_year, c.name
    FROM film AS f
    JOIN film_category AS fc ON f.film_id = fc.film_id
    JOIN category AS c ON fc.category_id = c.category_id
    WHERE LOWER(f.title) LIKE %s
    LIMIT %s OFFSET %s;
"""

FILM_GENRE_YEAR_QUERY = """
    SELECT f.title, f.release_year, c.name
    FROM film AS f
    JOIN film_category AS fc ON f.film_id = fc.film_id
    JOIN category AS c ON fc.category_id = c.category_id
    WHERE LOWER(c.name) = %s
    AND f.release_year BETWEEN %s AND %s
    LIMIT %s OFFSET %s;
"""


ALL_GENRES_QUERY = """
    SELECT DISTINCT name FROM category ORDER BY name;
"""

YEAR_RANGE_QUERY = """
    SELECT MIN(release_year), MAX(release_year) FROM film;
"""

#Запись в монго

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_DB = os.getenv('MONGO_DB')

CLIENT = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/"
    f"?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource={MONGO_DB}"
)



QUERY_DB = "final_project_100125dam_KrasnokutskijOksana"


PIPELINE = [
        {"$group": {"_id": "$query_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]




