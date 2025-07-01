from prettytable import PrettyTable
table = PrettyTable()

def main_menu():
    promt = """
        Menu:
        1. Searching film by name or by ganre and release year.
        2. Statistic
        0. Exit 
    """
    return int(input(promt))

def search_method_selection():
    return int(input("Select search method: 1 Searching film by name/2 Searching film by ganre and release year  "))
    

def film_name():
    return input("Input film title or part of title. ")

def film_ganre(ganres: list):
    print ("\n Available genres: ")
    for g in ganres:
        print (f"-{g}")
    return input("Input film ganre. ")
    
def film_release_year_min(min_year, max_year):
    return int(input(f"Input film release year min (from {min_year} to {max_year}): "))

def film_release_year_max(min_year, max_year):
    return int(input(f"Input film release year max (from {min_year} to {max_year}): "))

def continue_break_input():
    return input("Do you want continue? Yes\\No ")
    
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

def print_table_data(data: list[tuple]):
    table.field_names = ["Title", "Release year", "Genre"]
    table.add_rows(data)
    print(table)