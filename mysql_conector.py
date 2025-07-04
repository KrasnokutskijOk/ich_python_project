import pymysql
import settings
import ui
import error_logger


def connection(config: dict[str, any]) -> pymysql.connections.Connection:
    """
    Функция осуществляет подключение к базе данных MySQL

    """
    try:
        return pymysql.connect(**config)
    except pymysql.MySQLError as e:
        error_logger.log_error(f"MySQL connection failed: {e}")
        raise


def searching_film_by_name(db_conn: pymysql.connections.Connection, name: str) -> list[tuple[any, ...]]:
    """
    Функция принимает строковое значение и осуществляет поиск по названию фильма
    в базе данных MySQL
    
    
    """
    
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
            cursor.execute(settings.COUNT_FILM)
            total_count = cursor.fetchone()[0]

            offset = 0
            limit = 10
            results = []

            name = name.lower()
            while offset < total_count:
                cursor.execute(settings.FILM_NAME_QUERY, (f"%{name}%", limit, offset))
                rows = cursor.fetchall()

                if not rows:
                    ui.print_no_more_results()
                    break

                ui.print_table_data(rows)
                results.extend(rows)

                if ui.continue_break_input().lower() != "yes":
                    break

                offset += limit
            
            return results
            
    except Exception as e:
        error_logger.log_error(f"Error in searching_film_by_name: {e}")
        ui.print_error("Failed to search by name.")
        return []
    

def searching_film_by_ganre_and_release_year(
    db_conn: pymysql.connections.Connection,
    ganre: str,
    year_min: int,
    year_max: int
) - > list[tuple[any, ...]]:

    """
    Функция принимает строковое значение и осуществляет поиск по жанру и диапазону годов выпуска
    в базе данных MySQL
    
    
    """
    try:
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
                    ui.print_no_more_results()
                    break

                ui.print_table_data(rows)

                if ui.continue_break_input().lower() != "yes":
                    break

                offset += limit
            
            return results
            
    except Exception as e:
        error_logger.log_error(f"Error in search_by_genre_year: {e}")
        ui.print_error("Failed to search by genre and release year.")
        return []
    

def get_all_ganres(db_conn: pymysql.connections.Connection) -> list[str]:
    """
    Функция осущесвляет выборку всех жанров фильмов в базе данных MySQL

    """

    
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
            cursor.execute("SELECT name FROM category ORDER BY name;")
            return [row[0] for row in cursor.fetchall()]

    except Exception as e:
        error_logger.log_error(f"Error getting all genres: {e}")
        ui.print_error("Could not fetch genres.")
        return []



def get_year_range(db_conn: pymysql.connections.Connection) - tuple[int, int]:
    """
    Функция осущесвляет выборку минимального и максимального годов выпуска фильмов 
    в базе данных MySQL

    """
    try:
        with db_conn.cursor() as cursor:
            cursor.execute(f"USE {settings.DATABASE_MYSQL_NAME};")
            cursor.execute("SELECT MIN(release_year), MAX(release_year) FROM film;")
            return cursor.fetchone()

    except Exception as e:
        error_logger.log_error(f"Error getting year range: {e}")
        ui.print_error("Could not fetch year range.")
        return (2000, 2025)      