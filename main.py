import ui
import mysql_conector
import settings
#import log_writer
import log_stats

def get_action(action, db_conn):
    if action == 1:
        if action == 1.1:
            name = ui.film_name()
            #log_writer.query_writer(name)
            return mysql_connector.searching_film_by_name(db_conn, name)
            
        elif action == 1.2:
            ganre == ui.film_ganre()
            #log_writer.query_writer(ganre)
            release_year_min == ui.film_release_year_min()
            #log_writer.query_writer(release_year_min)
            release_year_max == ui.film_release_year_max()
            #log_writer.query_writer(release_year_max)
            return mysql_connector.searching_film_by_ganre_and_release_year(db_conn, ganre, release_year_min, release_year_max)
            
        else:
            print('Incorrect input')
    elif action == 2:
        stat == ui.statistic()
        return log_stats.show_statistics()
        
    else:
        print('Incorrect input')


def menu(db_conn):
    while (action := ui.main_menu()) != 0:
        result = get_action(action, db_conn)
        ui.print_table_data(result)
        

def main(db_conn):
    try:
        db_conn = mysql_conector.connection(settings.DATABASE_MYSQL_R)
        menu(result)
        db_conn.close()
    except pymysql.MySQLError as error:
        print(f"Connection or query error: ", error)
        

if __name__ == "__main__":
    main()