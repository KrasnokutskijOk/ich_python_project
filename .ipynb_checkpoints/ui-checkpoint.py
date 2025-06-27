def main_menu():
    promt = """
        Menu:
        1. Searching film:
        1.1. by name
        1.2. by ganre and release year
        2. Statistic
        0. Exit 
    """
    return int(input(promt))


def film_name():
    return input("Input film titel or part of titel.")

def film_ganre():
    return input("Input film ganre.")
    
def film_release_year_min():
    return input("Input film release year min.")

def film_release_year_max():
    return input("Input film release year max.")

def continue_break_input():
    return input("Do you want continue? Yes\\No")
    
def statistic():
    pass

def print_table_data(data: list[tuple]):
    for items in data:
        items = map(str, items)
        print('\t| '.join(items))
        