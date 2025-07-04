import ui
import mysql_conector
import settings
import log_writer
import log_stats
import error_logger
import pymysql
from pymysql.connections import Connection
from typing import Optional

def get_action(action: int, db_conn: Connection) -> Optional[list[tuple]]:
    """
    Функция регулирует действия программы в зависимости от действий пользователя
    
    """
    
    try:
        if action == 1:
            method = ui.search_method_selection()
        
            if method == 1:
                name = ui.film_name()
                result = mysql_conector.searching_film_by_name(db_conn, name)
                log_writer.write_log("keyword", {"keyword": name}, len(result))

                return result
            
            elif method == 2:
                ganres = mysql_conector.get_all_ganres(db_conn)
                year_min, year_max = mysql_conector.get_year_range(db_conn)
            
                ganre = ui.film_ganre(ganres)
                release_year_min = ui.film_release_year_min(year_min, year_max)
                release_year_max = ui.film_release_year_max(year_min, year_max)
                result = mysql_conector.searching_film_by_ganre_and_release_year(
                    db_conn, ganre, release_year_min, release_year_max
                )

                log_writer.write_log("ganre_year", {
                    "ganre": ganre,
                    "min_year": release_year_min,
                    "max_year": release_year_max
                }, len(result))
                return result
            
            else:
                ui.print_invalid_input()
                
        elif action == 2:
            log_stats.show_statistics()
        
        else:
            ui.print_invalid_input()

    except Exception as e:
        error_logger.log_error(f"Error in get_action: {e}")
        ui.print_error("Unexpected input or action error.")


def menu(db_conn: Connection) -> None:
    """
    Функция запускает главное меню

    """

    
    while True:
        try:
            action = ui.main_menu()
            if action == 0:
                break
            result = get_action(action, db_conn)
            if result:
                ui.print_table_data(result)
        except Exception as e:
            error_logger.log_error(f"Error in menu: {e}")
            ui.print_error("Unexpected input or action error.")
            

def main() -> None:
    """
    Функция осуществляет запуск программы и подключение к базе данных MySQL

    """
    try:
        db_conn = mysql_conector.connection(settings.DATABASE_MYSQL_R)
        menu(db_conn)
        db_conn.close()
    except pymysql.MySQLError as error:
        error_logger.log_error(f"MySQL error: {error}")
        ui.print_mysql_error(error)
    except Exception as e:
        error_logger.log_error(f"Unexpected error in main: {e}")
        ui.print_error("An unexpected error occured.")

if __name__ == "__main__":
    main()