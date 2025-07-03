from prettytable import PrettyTable
import error_logger

table = PrettyTable()

def main_menu():
    promt = """
        Menu:
        1. Searching film by name or by ganre and release year.
        2. Statistic
        0. Exit 
    """
    try:
        return int(input(promt))
    except ValueError as e:
        error_logger.log_error(f"Invalid input in main_menu: {e}")
        print_error("Please enter a number (0, 1, or 2).")
        return -1

def search_method_selection():
    try:
        return int(input("Select search method: 1 Searching film by name/2 Searching film by ganre and release year  "))
    except ValueError as e:
        error_logger.log_error(f"Invalid input in search_method_selection: {e}")
        print_error("Please enter 1 or 2.")
        return -1
    

def film_name():
    try:
        return input("Input film title or part of title. ")
    except Exception as e:
        error_logger.log_error(f"Error in film_name input: {e}")
        print_error("Error while reading film name.")
        return ""

def film_ganre(ganres: list):
    try:
        print("\nAvailable genres:")
        for g in ganres:
            print(f"- {g}")
        return input("Input film genre: ").strip()
    except Exception as e:
        error_logger.log_error(f"Error in film_genre input: {e}")
        print_error("Error while reading genre.")
        return ""
    
def film_release_year_min(min_year, max_year):
    try:
        return int(input(f"Input film release year min (from {min_year} to {max_year}): "))
    except ValueError as e:
        error_logger.log_error(f"Invalid input in film_release_year_min: {e}")
        print_error("Please enter a valid year.")
        return min_year

def film_release_year_max(min_year, max_year):
    try:
        return int(input(f"Input film release year max (from {min_year} to {max_year}): "))
    except ValueError as e:
        error_logger.log_error(f"Invalid input in film_release_year_max: {e}")
        print_error("Please enter a valid year.")
        return max_year

def continue_break_input():
    try:
        return input("Do you want continue? Yes\\No ")
    except Exception as e:
        error_logger.log_error(f"Error in continue_break_input: {e}")
        print_error("Error while reading input.")
        return "no"
    
def statistic():
    print("Showing statistics...\n")

def print_recent_statistic_title():
     print("Top 5 most recent queries:\n")

def print_single_recent_log(timestamp, query_type, params, results_count):
    print(f"[{timestamp}] Query Type: {query_type}, Params: {params}, Result: {results_count}")

def print_top_5_statistic_title():
    print("\nTop 5 most common query types:\n")

def print_top_5_query_type(query_type, count):
    print(f"  - {query_type}: {count} time(s)")

def  print_no_more_results():
    print("No more results. ")

def print_invalid_input():
    print("Invalid input. Please try again. ")

def print_mysql_error(error):
    print(f"MySQL connection or query error: {error} ")

def print_error(message: str):
    print(f"[ERROR] {message}")


def print_table_data(data: list[tuple]):
    try:
        table.clear_rows()
        table.field_names = ["Title", "Release year", "Genre"]
        table.add_rows(data)
        print(table)
    except Exception as e:
        error_logger.log_error(f"Error in print_table_data: {e}")
        print_error("Could not display table data.")