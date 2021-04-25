import pandas as pd
import numpy as np
from customer import Customer
from purchase import Purchase
from produce import Produce
from datetime import datetime as dt

# Imports the CSV file into a pandas DataFrame
customer_df = pd.read_csv('data/data_pull1.csv')
customer_dic = {}
produce_dic = {}

product_df = pd.read_csv('data/product_list.csv', skiprows=1)

# Drop unnecessary first column and add column names
product_df = product_df.drop('Unnamed: 0', axis=1)
product_df.columns = ['Category', 'Product', 'Unit', 'Color', 'Serving Size', 'Unit Weight', 'Correction', 'Comments']

# Create produce_dic with key [name of produce] and value [Produce object]
# Note: Unit Weight is not in the product_list csv, so it is default set to NaN
for index, row in product_df.iterrows():
    produce_dic[row['Product']] = Produce(row['Product'], row['Color'], row['Serving Size'], row['Unit Weight'], row['Correction'])


# Iterate over DF and convert the string of date and time into DateTime objects
customer_df['Visit Date'] = customer_df.apply(lambda row: dt.strptime(row['Visit Date'], '%Y-%m-%d %H:%M:%S'), axis=1)

# Iterate over rows and create customer dictionary and corresponding purchase dictionaries
for index, row in customer_df.iterrows():
    try:
        produce = produce_dic[row['Product'].rstrip()]
    except KeyError:
        # If produce is not in the produce list, create a Produce object with missing fields:
        # color="", serving_size=NaN, unit_weight=NaN, unit_price=actual unit price
        print('\"' + row['Product'].rstrip() + '" is not a produce in the list')
        produce = Produce(row['Product'].rstrip(), "", np.nan, np.nan, 0)
    produce.unit_price = row['Unit Price']

    # Add Customer object to dictionary if customer is not already in it
    loyalty_number = row['Loyalty Number']
    if loyalty_number not in customer_dic:
        customer_dic[loyalty_number] = Customer(loyalty_number, row['First Name'], row['Last Name'])
        
    # Adds a Purchase object to Customer's purchase dictionary
    purch = Purchase(row['Visit Date'], row['Location'], produce, row['Quantity'], row['Price'])
    customer_dic[loyalty_number].purchase_dict[produce.name] = purch

