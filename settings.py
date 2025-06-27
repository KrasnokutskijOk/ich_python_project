import main
import datetime


#Поиск фильмов My_SQL

DATABASE_MYSQL_R = {

    'host': 'ich-db.edu.itcareerhub.de',

    'user': 'ich1',

    'password': 'password',

    'charset': 'utf8mb4'

}

DATABASE_MYSQL_NAME = 'sakila'

COUNT_FilM = '''

    SELECT COUNT(film_id)

    FROM film

    '''

FILM_NAME_QUERY = f"SELECT f.title JOIN film_category as fc on f.film_id = fc.film_id join  FROM film as f WHERE LOWER(title) LIKE '% {main.get_action(name)}' or LOWER(title) LIKE '{main.get_action(name)} %' or LOWER(title) LIKE '% {main.get_action(name)} %'"

FILM_GANRE_RELEASE_YEAR = f"SELECT f.title, c.name FROM film as f JOIN film_category as fc on f.film_id = fc.film_id JOIN category as c on fc.category_id = c.category_id WHERE c.name = {main.get_action(ganre)} AND f.release_year BETWEEN {main.get_action(release_year_min)} AND {main.get_action(release_year_max)}"


#Запись в монго

# CLIENT = MongoClient("mongodb://ich_editor:verystrongpassword"
#  "@mongo.itcareerhub.de/?readPreference=primary"
#  "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit")

# MONGO_DB = "ich_edit"

# QUERY_DB = "final_project_100125dam_KrasnokutskijOksana"

# QUERY_LOG = [{
#  "timestamp": "2025-05-01T15:34:00",
 
# {"search_type": 
#     {"film_name": {main.get_action(name)}},
#     {"ganre_year": 
#         {"film_ganre": {main.get_action(ganre)}},
#         {"film_release_year_min": {main.get_action(release_year_min)}},
#         {"film_release_year_max": {main.get_action(release_year_max)}}
#          }
#     },
          
#  "results_count": 3
# }]

