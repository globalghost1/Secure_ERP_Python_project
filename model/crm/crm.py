""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
ID = 0
NAME = 1
EMAIL = 2
SUBSCRIBED = 3


def listing_customers():
    return data_manager.read_table_from_file(DATAFILE)


def adding_new_customer(new_customer_input):
    to_write_in_file = data_manager.read_table_from_file(DATAFILE)
    new_customer_input.insert(ID, util.generate_id())
    to_write_in_file.append(new_customer_input)
    data_manager.write_table_to_file(DATAFILE, to_write_in_file)


def updating_existing_customers(row, column, updated_data):
    client_data = listing_customers()
    for index, client in enumerate(client_data):
        if index == row:
            client[column] = updated_data
    data_manager.write_table_to_file(DATAFILE, client_data)


def deleting_customers(row):
    client_data = listing_customers()
    del client_data[row]
    data_manager.write_table_to_file(DATAFILE, client_data)


def subscribed_emails():
    client_data = data_manager.read_table_from_file(DATAFILE)
    e_mail_index = 2
    subscription_index = 3
    list_of_subscribed_emails = []
    for i in range(len(client_data)):
        if client_data[i][subscription_index] == "1" and "@" in client_data[i][e_mail_index]:
            list_of_subscribed_emails.append(client_data[i][e_mail_index])
    return list_of_subscribed_emails






    


