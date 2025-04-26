# Task 2: Read a CSV File
import traceback
import csv
# Create a function called read_employees that has no arguments
def read_employees():
    employee_dict = {}
    rows_list = []

#using the string with prefix r, since the backslashes were causing errors
    try:
        with open(r"C:\Users\kelly\OneDrive\Desktop\python_class\python_homework\csv\employees.csv", "r") as file:
            reader = csv.reader(file)
            #As you loop through the rows, store the first row in the dict using the key "fields"
            for i, row in enumerate(reader):
                if i == 0:
                    employee_dict["fields"] = row
                #Add all the other rows (not the first) to your rows list.
                else:
                    rows_list.append(row)
        #Add the list of rows (this is a list of lists) to the dict, using the key "rows".
        employee_dict["rows"] = rows_list
        #The function should return the dict.
        return employee_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
                print(f"Stack trace: {stack_trace}")
        #fixing error indicating to return none
        return None

employees = read_employees()
print(employees)

# Task 3: FInd the Column Index
def column_index(string):
    return employees["fields"].index(string)

employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_number]

    return row[first_name_column]

#Task 5: Find the employee. FUnction in a function 
#Create a function called employee_find.  This is passed one argument, an integer.  
def employee_find(employee_id):

    def employee_match(row):
         return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches

#Task 6: Find the employee with lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7: Sorts the rows by last name using Lambda
def sort_by_last_name():
    column_index_last_name = column_index("last_name")
    #key is equal to lambda so lambda can extract the value of lastname from each row
    employees["rows"].sort(key=lambda row: row[column_index_last_name])
    return employees["rows"]

#Task 8: Creat a dict for an Employee
def employee_dict(row):
    #the keys in the dict are columns headers from employee["fields"]
    column_headers = employees["fields"]
    #Do not include employee_id in the dict
    employee_id_value = column_index("employee_id")
    #create dict for employee, keys = column headers, values = everything else in row values, with condition where if i is equal to the employee id then skip
    emp_dict = {column_headers[i]: row[i] for i in range(len(column_headers)) if i != employee_id_value}

    return emp_dict

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    # the keys in the dict are the employee_ud from rows
    employee_id_value = column_index("employee_id")
    # the keys in the dict are the employee_ud from rows: for each key the value is employee_dict for that row
    all_emp_dict = {row[employee_id_value]: employee_dict(row) for row in employees["rows"]}
    return all_emp_dict

#Task 10: Use the os Module
import os

def get_this_value():
    #Environment variables are accessed via the os.getenv() function
    return os.getenv("THISVALUE")

#Task 11: Creating Your Own Module
import custom_module
#It should accept one parameter, which is the new secret to be set.
def set_that_secret(new_secret):
    #custom_module.set_secret(), passing the parameter
    custom_module.set_secret(new_secret)
#Add a line to your program to call set_that_secret, passing the new string of your choice.
set_that_secret("mynewsecret")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv

#You may want to create a helper function to avoid duplicating code.
#Each dict has fields and rows, just as the employees dict had. 
def reading_csv(csvpath):
    with open(csvpath) as csvfile:
        reader = csv.reader(csvfile)
        #fields is the column header
        fields = next(reader)
        # you create the list of rows for both minutes1 and minutes2, convert each row to a tuple.
        rows = [tuple(row) for row in reader]
        #{"fields": headers, "rows": data} 
    return {"fields": fields, "rows": rows}


#Create a function called read_minutes.  It takes no parameters.
def read_minutes():
    #It creates two dicts, minutes1 and minutes2, by reading ../csv/minutes1.csv and ../csv/minutes2.csv.
    minutes1 = reading_csv(r"C:\Users\kelly\OneDrive\Desktop\python_class\python_homework\csv\minutes1.csv")
    minutes2 = reading_csv(r"C:\Users\kelly\OneDrive\Desktop\python_class\python_homework\csv\minutes2.csv")
    #The function should return both minutes1 and minutes2.
    return minutes1, minutes2

#Store the values from the values it returns in the global variables minutes1 and minutes2
#v1, v2 = function()
minutes1, minutes2 = read_minutes()

#Task 13: Create minutes_set
def create_minutes_set():
    #creates two sets from the rows of minutes1 and minutes2 dicts.
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    #Combine the members of both sets into one single set.Union operation removes duplicates
    combined_set = set1 | set2
    return combined_set

#Store the value returned in the global variable minutes_set
minutes_set = create_minutes_set()

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    #Create a list from the minutes_set
    minutes_list = list(minutes_set)
    #map returns an object so in order to return to list we do list(map())
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return converted_list
#Store the return value in the minutes_list global
minutes_list = create_minutes_list()

#Task 15: Write out sorted list
def write_sorted_list():
    #Sort minutes_list in ascending order of datetime. datetime is the second element of tuple so x:x[1]
    asc_order_minutes_list = sorted(minutes_list, key=lambda x: x[1])
    #Call map again to convert the list and datetime back to a string, since im using strftime I don't need to pass second element of tuple(date) again
    convert_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), asc_order_minutes_list))
    #Open a file called ./minutes.csv
    with open('./minutes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        #The first row you write should be the value of fields the from minutes1 dict. 
        writer.writerow(minutes1["fields"])
        #The subsequent rows should be the elements from minutes_list.
        writer.writerows(convert_list)
    return convert_list



