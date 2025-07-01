import pymysql
import settings
import ui


def connection(config):
    return pymysql.connect(**config)


def searching_film_by_name(db_conn, name):
    with db_conn.cursor() as cursor:
        cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
        cursor.execute(settings.COUNT_FILM)
        total_count = cursor.fetchone()[0]

        offset = 0
        limit = 10
        results = []

        while offset < total_count:
            cursor.execute(settings.FILM_NAME_QUERY, (f"%{name.lower()}%", limit, offset))
            rows = cursor.fetchall()

            if not rows:
                print("No more results.")
                break

            ui.print_table_data(rows)
            results.extend(rows)

            if ui.continue_break_input().lower() != "yes":
                break

            offset += limit
            
        return results
    

def searching_film_by_ganre_and_release_year(db_conn, ganre, year_min, year_max):
    with db_conn.cursor() as cursor:
        cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
        
        count_query = """
                SELECT COUNT(*) FROM film AS f
                JOIN film_category AS fc ON f.film_id = fc.film_id
                JOIN category AS c ON fc.category_id = c.category_id
                WHERE LOWER(c.name) = LOWER(%s)
                AND f.release_year BETWEEN %s AND %s;
        """
        cursor.execute(count_query, (ganre, year_min, year_max))
        total_count = cursor.fetchone()[0]

        offset = 0
        limit = 10
        results = []

        while offset < total_count:
            data_query = """
                SELECT f.title, f.release_year, c.name AS genre
                FROM film AS f
                JOIN film_category AS fc ON f.film_id = fc.film_id
                JOIN category AS c ON fc.category_id = c.category_id
                WHERE LOWER(c.name) = LOWER(%s)
                AND f.release_year BETWEEN %s AND %s
                ORDER BY f.title
                LIMIT %s OFFSET %s;
            """
            cursor.execute(data_query, (ganre, year_min, year_max, limit, offset))
            rows = cursor.fetchall()
            results.extend(rows)

            if not rows:
                print("No more results.")
                break

            ui.print_table_data(rows)

            if ui.continue_break_input().lower() != "yes":
                break

            offset += limit
            
        return results
    

def get_all_ganres(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
        cursor.execute("SELECT name FROM category ORDER BY name;")
        return [row[0] for row in cursor.fetchall()]



def get_year_range(db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
        cursor.execute("SELECT MIN(release_year), MAX(release_year) FROM film;")
        return cursor.fetchone()