import ui
import mysql_conector
import settings
import log_writer
import log_stats
import pymysql

def get_action(action, db_conn):
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
            print('Incorrect input')
    elif action == 2:
        stat = ui.statistic()
        return log_stats.show_statistics()
        
    else:
        print('Incorrect input')


def menu(db_conn):
    while (action := ui.main_menu()) != 0:
        result = get_action(action, db_conn)
        if result:
            ui.print_table_data(result)
        

def main():
    try:
        db_conn = mysql_conector.connection(settings.DATABASE_MYSQL_R)
        menu(db_conn)
        db_conn.close()
    except pymysql.MySQLError as error:
        print(f"Connection or query error: ", error)
        

if __name__ == "__main__":
    main()