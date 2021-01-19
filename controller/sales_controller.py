from model.sales import sales
from view import terminal as view
from . import function_stash


def list_transactions():
    transactions_list = sales.get_data()
    view.print_message("List of transactions")
    view.print_table(sales.HEADERS, transactions_list)
    return transactions_list


def add_transaction():
    view.print_message("Enter a new transaction into the database\n ")
    questions = ["Please enter customer id: ",
                 "Please enter product name: ",
                 "Please enter price value: ",
                 "Please enter date of transaction(YYYY-MM-DD): "]
    new_transaction = view.get_inputs(questions)
    sales.insert_data(new_transaction)
    view.print_message("Successfully added transaction!")


def update_transaction():
    transactions_list = list_transactions()
    function_stash.update_logic("transaction", sales.update_data, sales.HEADERS, transactions_list)


def delete_transaction():
    transactions_list = list_transactions()
    function_stash.delete_logic("transaction", sales.remove_data, transactions_list)


def get_biggest_revenue_transaction():
    label = "The biggest single transaction is"
    biggest_transaction = sales.find_biggest_revenue_transaction()
    view.print_general_results(biggest_transaction, label)


def get_biggest_revenue_product():
    label = "The biggest revenue product is"
    biggest_revenue = sales.find_biggest_revenue_product()
    view.print_general_results(biggest_revenue, label)


def count_transactions_between():
    date_labels = ["Please enter date to count from (i.e. YYYY-MM-DD): ",
                   "Please enter date to count to (i.e. YYYY-MM-DD): "]
    time_frame = view.get_inputs(date_labels)
    date_from, date_to = time_frame[0], time_frame[1]
    transactions_between = sales.find_transactions_between(date_from, date_to)
    if len(transactions_between) > 1:
        view.print_message(f"\nTransactions between {date_from} to {date_to}")
        view.print_table(sales.HEADERS, transactions_between)
    else:
        view.print_general_results(transactions_between, f"Transaction between {date_from} to {date_to}")


def sum_transactions_between():
    date_labels = ["Please enter date to sum transactions from (i.e. YYYY-MM-DD): ",
                   "Please enter date to sum transactions to (i.e. YYYY-MM-DD): "]
    time_frame = view.get_inputs(date_labels)
    date_from, date_to = time_frame[0], time_frame[1]
    summed_transactions = sales.find_sum_transactions_between(date_from, date_to)
    view.print_general_results(summed_transactions, f"Sum of transactions between {date_from} to {date_to} equals")


def run_operation(option):
    view.clean()
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")
    print("\n")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
