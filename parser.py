import pandas as pd
from customer import Customer
from purchase import Purchase
from datetime import datetime as dt


# Imports the CSV file into a pandas DataFrame
customer_df = pd.read_csv('data/data_pull1.csv')
dic = {}
produce_dic = {}

product_df = pd.read_csv('data/product_list.csv')



# Iterate over DF and convert the string of date and time into DateTime objects
customer_df['Visit Date'] = customer_df.apply(lambda row: dt.strptime(row['Visit Date'], '%Y-%m-%d %H:%M:%S'), axis=1)

for index, row in customer_df.iterrows():
    # Change row['Product'] into a Product object
    purch = Purchase(row['Visit Date'], row['Location'], row['Product'], row['Quantity'], row['Price'])
    dic[row['Loyalty Number']] = Customer(row['Loyalty Number'], row['First Name'], row['Last Name'])
    dic[row['Loyalty Number']].purchase_dict[row['Product']] = purch

