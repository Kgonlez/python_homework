import pandas as pd 

df = pd.read_csv("../csv/employees.csv")

full_names = [f"{row['first_name']} {row['last_name']}" for index, row in df.iterrows()]
print("All Employee Names:", full_names)

names_with_e = [name for name in full_names if 'e' in name.lower()]
print("Names Containing 'e':", names_with_e)