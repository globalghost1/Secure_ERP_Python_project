from model.hr import hr
from view import terminal as view
from . import function_stash


def list_employees():
    employees_list = hr.get_employees_list()
    view.print_message("List of employees")
    view.print_table(hr.HEADERS, employees_list)
    return employees_list


def add_employee():
    view.print_message("Enter a new employee into the database\n")
    questions = [
        "Enter new employee's name: ",
        "Enter new employee's birth date(YYYY-MM-DD): ",
        "Specify new employee's department: ",
        "Specify new employee's clearance level: "]
    new_employee = view.get_inputs(questions)
    hr.create_new_employee(new_employee)
    view.print_message("Successfully added employee!")


def update_employee():
    employees_list = list_employees()
    function_stash.update_logic("employee", hr.update_employee, hr.HEADERS, employees_list)


def delete_employee():
    employees_list = list_employees()
    function_stash.delete_logic("employee", hr.delete_employee, employees_list)


def get_oldest_and_youngest():
    oldest_or_youngest_name = hr.find_names_oldest_youngest()
    view.print_general_results(
        oldest_or_youngest_name, 'The oldest and youngest employees are')


def get_average_age():
    avg_age = hr.average_age()
    view.print_general_results(avg_age, "Employees' average age")


def next_birthdays():
    input_date = view.get_input("Select the date to be checked since (YYYY-MM-DD)")
    result = hr.employees_birthday(input_date)
    view.print_message("Employees having their birthday with in 2 weeks \n\t" + str(result))


# def next_birthdays():
#     input_date = view.get_input('Select the date to be checked since (YYYY-MM-DD)')
#     result = hr.employees_birthday(input_date)
#     view.print_general_results(hr.birthday(input_date), 'Employees having their birthday with in 2 weeks ')


'''

def next_birthdays():
    data = data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(data, hr.HEADERS)
    name, days = hr.next_birth()
    for i in range(len(name)):
        view.print_message(f"\n Next birthday has: {data[int(name[i])][1]}")
        view.print_message(f"Days left: {int(0-int(days[i]))}")
    view.get_input("")

    '''


def count_employees_with_clearance():
    given_clr_lvl = view.get_input('Specify the minimum clearance level')
    qty = hr.num_of_employees_clr_lvl(given_clr_lvl)
    view.print_general_results(
        qty, 'Number of employees above or equal to this criteria is')


def count_employees_per_department():
    num_per_departament = hr.num_of_employees_per_departament()
    view.print_general_results(
        num_per_departament, 'Departments with their inner employees quantities')


def run_operation(option):
    view.clean()
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")
    print("\n")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
