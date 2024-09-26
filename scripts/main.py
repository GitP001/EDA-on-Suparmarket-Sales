# Copy of Ashaab Rizvi's work; Kaggle, Supermaket sales -  Analysis and Visualization

# 1. Data Exploration
# 2. Data Cleaning
# 3. Exploratory Data Analysis
'''
- Finding relationships most correlated columns
- Finding the most busy city, payment type, branch
- Visualizing a Gender based comparison for different product type
- Visualizing a City based comaparision for different product type
- Finding which payment method is used more often at a particular city, 
    branch and for which product type
- Finding which branch has a better sale for which product
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv('/Users/kyungtaekpark/Desktop/Project/Supermarket Sales EDA/data/supermarket_sales.csv')
sales.head()
sales.shape # To check number of rows and columns
sales.columns
sales.dtypes  # Here, date is object, so we want to convert it into Datetime
sales['Date'] = pd.to_detetime(sales['Date'])
sales['Date']
sales.dtypes # Here, we have changed date to datetime from object
sales.set_index('Date', inplace=True)
sales.head()
sales.describe() # Statistical Summary
sales.isnull().sum() # To check null values
# Now we want to first handle Unit Price Column by using mean value
avg_unit_price = sales["Unit price"].astype("float").mean(axis=0)
sales["Unit price"].replace(np.nan, avg_unit_price, inplace=True)
# For Quantity we will use Mode value
from scipy import stats
mode=stats.mode(sales['Quantity'])

print(mode)

sales['Quantity'].replace(np.nan, "mode", inplace=True)
# For rest remaining values we will simply drop them
sales.dropna(inplace==True)

