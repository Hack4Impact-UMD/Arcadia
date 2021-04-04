import pandas as pd
from datetime import datetime as dt

# Imports the CSV file into a pandas DataFrame
customer_df = pd.read_csv('data/data_pull1.csv')

# Iterate over DF and convert the string of date and time into DateTime objects
customer_df['Visit Date'] = customer_df.apply(lambda row: dt.strptime(row['Visit Date'], '%Y-%m-%d %H:%M:%S'), axis=1)