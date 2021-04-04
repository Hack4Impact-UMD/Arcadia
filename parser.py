import pandas as pd
from datetime import datetime as dt

# Imports the CSV file into a pandas DataFrame
customer_df = pd.read_csv('data/data_pull1.csv')

# Conversion of the string date and time into a python DateTime object
datetime_object = dt.strptime('2017-07-20 19:57:20', '%Y-%m-%d %H:%M:%S')