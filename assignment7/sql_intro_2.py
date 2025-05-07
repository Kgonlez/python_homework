import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('../db/lesson.db')  
#print("Connected to database.")

query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM 
    line_items
JOIN 
    products 
ON 
    line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
#print(df.head())

#Add a column to the DataFrame called "total". 
df['total'] = df['quantity'] * df['price']
#print(df.head())

#Group by product_id
grouped_df = df.groupby('product_id').agg({
    'line_item_id' :'count',
    'total':'sum',
    'product_name':'first'
}).reset_index()
#print(grouped_df.head())

#Sort by product_name
grouped_df = grouped_df.sort_values('product_name')
#print(grouped_df.head())

grouped_df.to_csv('order_summary.csv', index= False)
print("\norder_summary.csv has been written successfully.")

conn.close()