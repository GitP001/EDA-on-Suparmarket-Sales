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

# DATA EXPLORATION AND CLEANING

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
sales.dropna(inplace=True)
sales.isnull().sum() # Finally we can see No null values at this point
sales.corr()
np.round(sales.corr(),2)

# EXPLORATORY DATA ANALYSIS

plt.figure(dpi=125)
sns.heatmap(np.round(sales.corr(), 2), annot=True)
plt.show()
# The best correlated are Tax 5%, Total, Gross Income and cogs i.e Cost of Goods sold with correlation of 1.
# Also, the above mentioned all has a good correlation of 0.71 with Quantity

plt.figure(figsize=(12,6), dpi=100)
sns.regplot(x='Tax 5%', y='gross income', data=sales, color='Red')
plt.xlabel('Tax 5%')
plt.ylabel('Gross Income')
plt.show()

plt.figure(figsize=(12,6), dpi=100)
sns.regplot(x='Quantity', y='cogs', data=sales, color='green')
plt.xlabel('Quantity')
plt.ylabel('Cost of Goods Sale')
plt.title('Quantity v Cost of Goods Sale', fontsize=15)
plt.show()

plt.figure(figsize=(12,6), dpi=100)
sns.regplot(x='Unit price', y='gross income', data=sales, color='blue')
plt.xlabel('Unit Price')
plt.ylabel('Gross Income')
plt.title('Unit Price v Gross Income', fontsize=15)
plt.show()

# Below is to see the distribution of different ratings
plt.figure(dpi=125)
sns.distplot(sales['Rating'], kde=False)
plt.show()

# Now Let's find the mean rating 

# To find Mean Rating,
plt.figure(dpi=125)
sns.displot(sales['Rating'], kde=False)
plt.axvline(x=np.mean(sales['Rating']), c='green', label='Mean Rating')
plt.legend()
plt.show()

# Plotting Histogram for all
sales.hist(figsize=(12,12))
plt.show()

# Analysis of Branch, City and Product Type

# Branch Count
plt.figure(dpi=125)
sns.countplot(sales['Branch'])
plt.xlabel('Branch Name')
plt.ylabel('Count')
plt.title('Which Branch is the most busy?')
A,B,C=sales.Branch.value_counts()

print('Branch A -', A)
print('Branch B -', C)
print('Branch C -', B)

plt.show()

# Branch A - 340 / Branch B - 328 / Branch C - 332

plt.figure(dpi=125)
sns.countplot(sales['Payment'])
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.title('Which Payment Method is most used?')
A,B,C = sales.Payment.value_counts

print('E-wallet -',A)
print('Cash -', B)
print('Credit Card -', C)

plt.show()

# E-wallet - 345 / Cash - 344 / Credit Card - 311

plt.figure(dpi=125)
sns.countplot(sales['City'])
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Which City is most busy?')
A,B,C=sales.City.value_counts()

print('Yangon -',A)
print('Naypyitow -',C)
print('Mandalay -', B)

plt.show()

# Yangon - 340 / Naypyitow - 328 / Mandalay - 332

plt.figure(dpi=125)
sns.countplot(sales['Gender'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Count of Gender')
A,B=sales.Gender.value_counts()

print('Male -',B)
print('Female -',A)

plt.show()

# Male - 499 / Female - 501

# Visualizing a Gender based comparision related to Product Type
sns.catplot(x='Product line', y='Unit price', hue='Gender', data=sales, aspect=2)
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.show()

# Jitter=False is good to find the relation better, so

sns.catplot(x='Product line', y='Unit price', hue='Gender', data=sales, aspect=2, jitter=False)
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.show()

plt.figure(dpi=125)
sns.countplot(y='Product line', hue='Gender', data=sales)
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

# We see that, in Health & Beuty, Males are much more than Females whereas in Fashion accessories,
#   Food & beverages and Sports & Travel Females are more and in the rest there is not much significant difference.

# Visualizing a City based comparision related to Product Type

sns.catplot(x='Product line', y='Unit price', hue='City', kind='swarm', data=sales, aspect=2)
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.show()

sns.catplot(x='Product line', y='Unit price', hue='City', data=sales, aspect=2, jitter=False)
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.show()

plt.figure(dpi=125)
sns.countplot(y='Product line', hue='City', data=sales)
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

# Yangon leads at Home & Lifestyle and Electronic accessories.
# Naypyitaw leads at Food & Beverages and Fashion accessories.
# Mandalay leads at Sports & Travel and Health & Beauty.

# Finding the most used payment method for Product Type, Branch and City
plt.figure(dpi=125)
sns.countplot(y='Product line', hue='Payment', data=sales)
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

plt.figure(dpi=125)
sns.countplot(y='Branch', hue='Payment', data=sales)
plt.xlabel('Count')
plt.ylabel('Branch')
plt.show()

plt.figure(dpi=125)
sns.countplot(y='City', hue='Payment', data=sales)
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

# Finding Which Branch has better sale for a particular product type

plt.figure(dpi=125)
sns.countplot(y='Product line', hue='Branch', data=sales)
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

# Boxen plot for Rating and Quantity
# Definition of Boxen Plot:
# The Boxen plot is very similar to box plot, except for the fact that it plots different quartile values.
#   By plotting different quartile values, we are able to understand the shape of
#       the distribution particularly in the head end and tail end. 

sns.catplot(y='Rating', x='Quantity', data=sales, kind='boxen', aspect=3)
plt.xlabel('Quantity')
plt.ylabel('Rating')
plt.show()

from wordcloud import WordCloud

plt.subplots(figsize=(20,8))
wordcloud = WordCloud(background_color='White', width=1920, height=1080).generate(" ".join(sales['Product line']))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('cast.png')
plt.show()