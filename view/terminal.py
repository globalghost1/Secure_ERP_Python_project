import os
import datetime
from copy import deepcopy


def clean():
    os.system("cls || clear")
    show_now = datetime.datetime.now().strftime("%A, %d-%m-%Y\nTime: %H:%M:%S ")
    print('Today is:', show_now)
    print("\n")


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for number, element in enumerate(list_options):
        print(f"{number}) {element}")
    print()


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == float:
        formatted_float = "{:.2f}".format(result)
        print(f'{label}: {formatted_float}')
    elif type(result) == int:
        print(f'{label}: {result} ')
    elif type(result) == list or type(result) == tuple:
        print(f'{label}: ')
        k = 1
        for i in result:
            print(f'{i} ', end="")
            if k != len(result):
                print(f'; ', end="")
                k += 1
        print()
    elif type(result) == dict:
        print(label)
        k = 1
        for elem in result:
            print(f'{elem}: {result[elem]}', end="")
            if k != len(result):
                print(f'; ', end="")
                k += 1
            print()
        print()
    else:
        print(f"{label}: {result}")


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(headers, table):
    """Prints tabular data like above.
    Args:
        headers: list of headers - headers to print out on top of table
        table: list of lists - the table to print out
    """
    table = populate_index_rows(headers, table)
    column_widths = count_column_widths(table)
    table_width = count_table_width(column_widths)
    for index, rows in enumerate(table):
        if index == 0:
            print(f"/" + "-" * (table_width - 1), end="\\\n")
        else:
            print(f"|", end="")
            for col_index, column in enumerate(rows):
                print("-" * (column_widths[col_index] + 1) + "|", end="")
            print()
        if index == 0:
            print("|", end="")
            for col_index, column in enumerate(rows):
                print(f"{column.center(column_widths[col_index])}", end=" |")
            print()
        else:
            print("|", end="")
            for col_index, column in enumerate(rows):
                print(f"{column.center(column_widths[col_index])}", end=" |")
            print()
        if index == len(table) - 1:
            print(f"\\" + "-" * (table_width - 1), end="/\n")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label)


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    answer_list = []
    for label in labels:
        answer = input(label)
        answer_list.append(answer)
    return answer_list


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)


def count_column_widths(table):
    columns_max_width = []
    for row_index, rows in enumerate(table):
        for index, column in enumerate(rows):
            if row_index == 0:
                columns_max_width.append(len(rows) + 1)
            if len(column) >= columns_max_width[index]:
                columns_max_width[index] = len(column) + 1
    return columns_max_width


def count_table_width(columns_max_width):
    return sum(columns_max_width) + (len(columns_max_width) * 2)


def populate_index_rows(headers, table):
    indexed_table_with_headers = deepcopy(table)
    copied_headers = deepcopy(headers)
    indexed_table_with_headers.insert(0, copied_headers)
    for index, row in enumerate(indexed_table_with_headers):
        if index == 0:
            row.insert(0, "#")
        else:
            row.insert(0, str(index))
    return indexed_table_with_headers
