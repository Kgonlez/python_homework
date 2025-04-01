#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd
import json

data = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age": [25,30,35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

#Make a copy of the origional df
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000,80000,90000]
print(task1_with_salary)

#Make a copy task1_with_salary in a variablenames task1_older
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print(task1_older)

#save the df to a csv file 
task1_older.to_csv("employees.csv", index= False)
print("csv file 'employees.csv' has been saved.")



#Task 2: Loading Data from CSV and JSON
task2_employees= pd.read_csv(r"C:\Users\kelly\OneDrive\Desktop\python_class\python_homework\assignment3\employees.csv")
print(task2_employees)

json_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary" : 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary" : 95000}
]

with open("additional_employees.json", "w") as json_file:
    json.dump(json_data, json_file)

#Load json file into a new df 
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

#Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees],ignore_index= True)
print(more_employees)
                         

#Task 3: Data Inspection- Using Head, tail, and Infor Methods
#Use the head() methods
first_three = more_employees.head(3)
print(first_three)

#Use the tail() method
last_two = more_employees.tail(2)
print(last_two)

#Get the shape of a dataframe
employee_shape = more_employees.shape
print(employee_shape)

#use info() method
more_employees.info()


# Task 4: Data Cleaning 
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()
print(clean_data)

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors= "coerce")
print(clean_data)

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"].replace(["unknown", "n/a"], pd.NA), errors= "coerce")
print(clean_data)

clean_data["Age"]= clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)