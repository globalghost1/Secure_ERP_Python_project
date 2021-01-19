from datetime import date, timedelta
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
ID = 0
NAME = 1
DATE_OF_BIRTH = 2
DEPARTMENT = 3
CLEARANCE = 4


def get_employees_list():
    return data_manager.read_table_from_file(DATAFILE)


def create_new_employee(new_employee):
    employee_list = get_employees_list()
    new_id = util.generate_id()
    new_employee.insert(ID, new_id)
    employee_list.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, employee_list)


def update_employee(row, column, updated_data):
    employee_list = get_employees_list()
    for index, employee in enumerate(employee_list):
        if index == row:
            employee[column] = updated_data
    data_manager.write_table_to_file(DATAFILE, employee_list)


def delete_employee(row):
    employee_list = get_employees_list()
    del employee_list[row]
    data_manager.write_table_to_file(DATAFILE, employee_list)


def find_names_oldest_youngest():
    employee_list = get_employees_list()
    oldest_employee = min(employee_list, key=lambda employee: employee[2])
    youngest_employee = max(employee_list, key=lambda employee: employee[2])
    return oldest_employee[1], youngest_employee[1]


def calculate_age(birthday_date):
    year, month, day = [int(f) for f in birthday_date.split('-')] # zamienia datę rozdzieloną '-' na int 
    birthday_date = date(year, month, day)
    today = date.today() # dzisiejsza data
    years = today.year - birthday_date.year
    if today.month < birthday_date.month or (today.month == birthday_date.month and today.day < birthday_date.day):
        years -= 1 # - 1 rok jak jeszcze nie było urodzin w obecnym roku. 
    return years


def average_age():
    employees_list = get_employees_list()
    avg_employee_age = sum(calculate_age(employee[2]) for employee in employees_list)/len(employees_list)
    return avg_employee_age


def employees_birthday(input_date):
    
    input_year = int(input_date[0:4])
    input_month = int(input_date[5:7])
    input_day = int(input_date[8:10])
    input_date = date(input_year, input_month, input_day) 
    result = []

    list_employee = data_manager.read_table_from_file(DATAFILE, separator=';')
    for employee in list_employee: 
        employee_date=employee[2]
        employee_month = int(employee_date[5:7])
        employee_day = int(employee_date[8:10])

        this_date = date(input_year, employee_month,employee_day) 
        delta = this_date - input_date 
        delta = delta.days #int
       
        
        if (delta <= 14 and delta >=0) : 
            result.append(employee[1]) 

    return result


# def coming_birthday(input_date):
#     employees_list = get_employees_list()

#     year, month, day = [int(f) for f in input_date.split('-')]
#     input_date = date(year, month, day)
    
#     fortnite_to_birthday = input_date + timedelta(days = 14)
#     results = []

#     for employee in employees_list:
#         birthday_month, birthday_day = [int(f) for f in employee[2].split('-')]
#         birthday_date = date(year, birthday_month, birthday_day)
#         next_birthday_date = date(year+1, birthday_month, birthday_day) 
#         if (birthday_date >= input_date and birthday_date <= fortnite_to_birthday) or (next_birthday_date >= input_date and next_birthday_date <= fortnite_to_birthday):
#             results.append(employee[1])
#     return results

'''

def next_birth():
    q = []
    r = []
    teraz = datetime.datetime.now()
    dzien = str(teraz.day) 
    miesiac = str(teraz.month) 
    b = (int(miesiac) - 1) * 30
    c = int(dzien)
    e = b + c 
    y=data_manager.read_table_from_file(data_manager.DATAFILE, separator=';')
    day_all = []
    for i in range(len(y)):
        k = y[i]
        b1 = (int(k[2][5:7]) - 1 ) * 30
        c1 = int(k[2][8:10])
        e1 =  b1 + c1 
        day_emp = int(e) - int(e1)
        day_all.append(day_emp)

    for i in range(len(day_all)):
        if day_all[i] < 0 and day_all[i] >= -14:
            q.append(day_all[i])
            r.append(i)
        else:
            pass

    return  r, q

    '''


def num_of_employees_clr_lvl(given_clr_lvl):
    employees_list = get_employees_list()
    results = 0
    for employee in employees_list:
        if int(employee[4]) >= int(given_clr_lvl):
            results += 1
    return results


def num_of_employees_per_departament():
    employees_list = get_employees_list()
    results = {}
    for employee in employees_list:
        if employee[3] in results:
            results[employee[3]] += 1
        else:
            results[employee[3]] = 1
    return results
