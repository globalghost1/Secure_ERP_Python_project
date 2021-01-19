""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
ID = 0
CUSTOMER = 1
PRODUCT = 2
PRICE = 3
DATE = 4


def get_data():
    return data_manager.read_table_from_file(DATAFILE)


def insert_data(new_transaction):
    transaction_data = get_data()
    new_id = util.generate_id()
    new_transaction.insert(ID, new_id)
    transaction_data.append(new_transaction)
    data_manager.write_table_to_file(DATAFILE, transaction_data)


def update_data(row, column, updated_data):
    transaction_data = get_data()
    row_to_update = transaction_data[row]
    row_to_update[column] = updated_data
    data_manager.write_table_to_file(DATAFILE, transaction_data)


def remove_data(row):
    transaction_data = get_data()
    del transaction_data[row]
    data_manager.write_table_to_file(DATAFILE, transaction_data)


def find_biggest_revenue_transaction():
    biggest_transaction = 0
    biggest_transaction_index = 0
    transactions_list = get_data()
    for index, transaction in enumerate(transactions_list):
        if float(transaction[PRICE]) > biggest_transaction:
            biggest_transaction = float(transaction[PRICE])
            biggest_transaction_index = index
    return transactions_list[biggest_transaction_index]


def find_biggest_revenue_product():
    product_occurrence = {}
    product_price = {}
    transactions_list = get_data()
    for transaction in transactions_list:
        product_price[transaction[PRODUCT]] = float(transaction[PRICE])
        if transaction[PRODUCT] in product_occurrence:
            product_occurrence[transaction[PRODUCT]] += 1
        else:
            product_occurrence[transaction[PRODUCT]] = 1
    all_product_revenue = {key: product_price[key] * product_occurrence[key]
                           for key in product_occurrence}
    biggest_revenue_product = max(all_product_revenue, key=all_product_revenue.get)
    return biggest_revenue_product


def find_transactions_between(date_from, date_to):
    transactions_list = get_data()
    transactions_between = []
    for transaction in transactions_list:
        if date_from <= transaction[DATE] <= date_to:
            transactions_between.append(transaction)
    return transactions_between


def find_sum_transactions_between(date_from, date_to):
    transactions_list = get_data()
    transactions_between = []
    for transaction in transactions_list:
        if date_from <= transaction[DATE] <= date_to:
            transactions_between.append(float(transaction[PRICE]))
    summed_transactions = sum(transactions_between)
    return summed_transactions
