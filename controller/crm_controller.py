from model.crm import crm
from view import terminal as view
from . import function_stash


def list_customers():
    customers_list = crm.listing_customers()
    view.print_message("List of customers")
    view.print_table(crm.HEADERS, customers_list)
    return customers_list


def add_customer():
    new_customer_input = view.get_inputs(["Please provide new user name: ",
                                          "Please provide new user e-mail address: ",
                                          "Please provide 1 if subscribed, 0 if not: "])
    crm.adding_new_customer(new_customer_input)
    view.print_message("Successfully added customer!")


def update_customer():
    customers_list = list_customers()
    function_stash.update_logic("customer", crm.updating_existing_customers, crm.HEADERS, customers_list)



def delete_customer():
    customers_list = list_customers()
    function_stash.delete_logic("customer", crm.deleting_customers, customers_list)


def get_subscribed_emails():
    label = "\nLists of subscribed e-mails is below"
    view.print_general_results(crm.subscribed_emails(), label)
    

def run_operation(option):
    view.clean()
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")
    print("\n")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
