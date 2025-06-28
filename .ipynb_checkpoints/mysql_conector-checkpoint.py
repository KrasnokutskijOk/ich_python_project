import pymysql
import settings
import ui



def connection(config):
    conn = pymysql.connect(**config)
    return conn



def searching_film_by_name(db_conn, param):
    with db_conn.coursor() as coursor:
        cursor.execute(f'USE {settings.DATABASE_MYSQL_NAME}')
        cursor.execute(settings.COUNT_FilM)
        data = coursor.fetchall()
        count_total = data[0][0]

        next10 = 0

        while next10 < count_total:
            query = ui.continue_break_input()
            if query == "Yes":
                next10 += 10   
                cursor.execute(settings.FILM_NAME_QUERY)
                return cursor.fetchall()
            else:
                break

def searching_film_ganre_and_release_year(db_conn, param):
    with db_conn.coursor() as coursor:
        cursor.execute(f'USE {settings.DATABASE_MYSQL_NAME}')
        cursor.execute(COUNT_FilM)
        data = coursor.fetchall()
        count_total = data[0][0]

        next10 = 0

        while next10 < count_total:
            query = ui.continue_break_input()
            if query == "Yes":
                next10 += 10   
                cursor.execute(settings.FILM_GANRE_RELEASE_YEAR)
                return cursor.fetchall()
            else:
                break


