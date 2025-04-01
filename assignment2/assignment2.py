import csv
import os
import custom_module
from datetime import datetime

print("-------------------------------PRINT TASK #2")

def read_employees():
    data_dict = dict()
    data_list = list()
    
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            data_dict['fields'] = next(reader)
            for row in reader:
                data_list.append(row)
            data_dict['rows'] = data_list
    except Exception as e:
        print(e)
    return data_dict

employees = read_employees()
print(employees)      


print("------------------------------------------TASK 3")

def column_index(string):
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            title_columns = next(reader)
            return title_columns.index(string)
    except Exception as e:
        print(e)  
        
print(column_index("first_name"))        
print(column_index("last_name"))        
print(column_index("phone"))      

employee_id_column = ''
employee_id_column = column_index("employee_id") 
print(employee_id_column) 
    

print("------------------------------------------TASK 4")

print(type(employees))


def first_name(row_number):
    try:
        index = column_index("first_name")
        emp_first_name = employees['rows'][row_number][index]
        return emp_first_name
    except Exception as e:
        print(e)

print(first_name(3))
                 
print("------------------------------------------TASK 5")

def employee_find(employee_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id
        matches = list(filter(employee_match, employees['rows']))
        return matches
    except Exception as e:
        print(e)

print(employee_find(7))

print("------------------------------------------TASK 6")

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches

print(employee_find_2(7))
print(employees['rows'])
print("------------------------------------------TASK 7")

def sort_by_last_name():
    try:
        last_name_index = column_index("last_name")
        employees['rows'].sort(key= lambda row: row[last_name_index])
    except Exception as e:
        print(e)
    return employees['rows']

sort_by_last_name()
print("print employees dict", employees)

print("------------------------------------------TASK 8")
def employee_dict(row):
    try:
        dict = {}
        dict['first_name'] = row[1]
        dict['last_name'] = row[2]
        dict['phone'] = row[3]
        
        return dict
    except Exception as e:
        print(e)
        
print(employee_dict(['10', 'Kelli', 'Bowman', '+379 (843)240-1818x77648']))

print("------------------------------------------TASK 9")
def all_employees_dict():
    try:
        dict_of_dicts = {}
        for row in employees['rows']:
            employee_id = row[0]
            employee_data = employee_dict(row)
            
            dict_of_dicts[employee_id] = employee_data
        return dict_of_dicts
    except Exception as e:
        print(e)
        
print(all_employees_dict())
print("------------------------------------------TASK 10")

def get_this_value():
    try:
        return os.getenv("THISVALUE")
        
    except Exception as e:
        print(e)
        
get_this_value()
print("------------------------------------------TASK 11")

def set_that_secret(new_secret):
    try:
        custom_module.set_secret(new_secret)
        set_that_secret()
        print(custom_module.secret)
    except Exception as e:
        print(e)
print("------------------------------------------TASK 12")
def read_minutes():
    try:
        minutes1 = dict()
        list1 = list()
        minutes2 = dict()
        list2 = list()
        
        with open("../csv/minutes1.csv", 'r') as file:
            reader = csv.reader(file)
            minutes1['fields'] = next(reader)
            for row in reader:
                tupled_row = tuple(row)
                list1.append(tupled_row)
            minutes1['rows'] = list1
            
            # print(minutes1)
            
        with open("../csv/minutes2.csv", 'r') as file:
            reader = csv.reader(file)
            minutes2['fields'] = next(reader)
            for row in reader:
                tupled_row = tuple(row)
                list2.append(tupled_row)
            minutes2['rows'] = list2
            # print("----------------", minutes2)            
    except Exception as e:
        print(e)
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(read_minutes()) 


print("------------------------------------------TASK 13")
def create_minutes_set():
    try:
        set1 = set(minutes1['rows'])
        set2 = set(minutes2['rows'])
        combined_set = set1 | set2
        print("combined_set", combined_set)
        return combined_set
    except Exception as e:
        print(e)

minutes_set = create_minutes_set()
print("------------------------------------------TASK 14")
def create_minutes_list():
    try:
        list1 = list(minutes_set)
        minutes_list = list(map(lambda x: tuple([x[0], datetime.strptime(x[1], "%B %d, %Y")]),list1))
        print(minutes_list)
        return minutes_list  
        
    except Exception as e:
        print(e)

minutes_list = create_minutes_list()
print("------------------------------------------TASK 15")

def write_sorted_list():
    try:
        sorted_list = sorted(minutes_list, key=lambda x: x[1])
        tupled_list = list(map(lambda x: tuple([x[0], datetime.strftime(x[1], "%B %d, %Y")]),sorted_list))
        with open("./minutes.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            writer.writerows(tupled_list)
            return tupled_list
    except Exception as e:
        print(e)
sorted_minutes = write_sorted_list()                                                          