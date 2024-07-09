#!/usr/bin/env python
# coding: utf-8

# # Pandas for Data Analysis

# In[1]:


import pandas as pd
import numpy as np


# # Filtering and Ordering

# ## Filtering on Columns

# In[224]:


df = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/laptop_prices.csv', encoding = 'ISO-8859-1')


# In[225]:


df.shape


# In[226]:


pd.set_option('display.max.rows', 1400) # To see the maximum rows
pd.set_option('display.max.columns', 15) # To see the maximum columns


# In[227]:


df


# In[228]:


df[['Company', 'Product', 'Price_usd']] # To see the data in the columns "Company, Product, Price_usd"


# In[229]:


df.loc[:2, ['Company', 'Product', 'Price_usd']] # To see the data in the columns "Company, Product, Price_usd" and 3 rows 


# In[230]:


df.iloc[:3, [1,2,12]] # To see the data in the columns "Company, Product, Price_usd" by index numbers and 3 rows


# In[ ]:





# In[254]:


df.filter(items = ['Company', 'Product', 'Price_usd'], axis = 1) 

# To filter the data in the columns "Company, Product, Price_usd"


# ## Filtering on Rows

# In[255]:


df[df['Company'] == 'Apple'] #To extract the data of "Apple" laptops


# In[256]:


df[(df['Company'] == 'Apple') & (df['Ram'] == '16GB')] 

# To extract the data of "Apple" laptops, AND 16GB of Ram


# In[251]:


df[(df['Company'] == 'Apple') | (df['Ram'] == '16GB')] 

# To extract the data of "Apple" laptops, OR 16GB of Ram


# In[257]:


df[df['Company'].isin(['Apple', 'Dell']) & (df['Ram'] == '16GB')]

# To extract the data of "Apple and Dell" laptops, AND 16GB of Ram


# In[258]:


df[df['Price_usd'] >= 5000]

# To extract the data that has price of >=5000


# In[237]:


df[df['Price_usd'] == 5388.9] 

#To pull the data that has the price of 5388.9


# In[238]:


df[df['Price_usd'] <= 200]

#To pull the data that has the price of <= 200


# In[239]:


df.loc[:3]

#We are looking at the names. So these are the named values, which is going to include number 3.


# In[240]:


df.iloc[:3] 

# We are looking at the integer based locations. There are the actual numbers behind the names. And its pulling first 3 rows


# In[259]:


df.iloc[[0,5,10,20]]

# To pull the data from the rows 0,5,10,20


# In[260]:


df.filter(items = [0,5,10,20], axis = 0)

# To filter the data from the rows 0,5,10,20


# ## Filtering using String Methods

# ####  1. ".contains( )"  - method is used to check if each element in a Series contains a specified string or pattern. This method is particularly useful when you want to filter rows based on whether a specific substring exists in the values of a column.
# 
# ####  2. ".str.startswith( )" -  method is used to check if each element in a Series starts with a specified string.
# 
# ####  3. ".str.endswith( )" -  method is used to check if each element in a Series ends with a specified string.
# 
# ####  4. ".duplicated( )" -  method is used to identify duplicate rows in a DataFrame
# 
# ####  5. ".str.match( )" -  method is used to check if each element in a Series matches a specified regular expression pattern

# In[243]:


df[df['Product'].str.contains('MacBook')] #Pulls the "MacBook" that contain in Product


# In[244]:


df[df['Product'].str.contains('MacBook') == False] #Pulls the "MacBook" that do not contain in Product


# In[262]:


df[(df['Product'].str.contains('MacBook')) & (df['Memory'].str.contains('SSD'))] 

#To pull the data that contains the word 'MacBook'and 'SSD'


# In[246]:


df[df['Product'].str.startswith('Mac')]

#To pull the data that startswith the word 'Mac'


# In[247]:


df[df['Product'].str.endswith('14')]

#To pull the data that endswith the number 14 in 'Product' column


# In[248]:


df[df['Price_usd'].duplicated()].sort_values(by = 'Price_usd')

#To pull the data that has duplicates in 'Price_usd' column and sorting them in Ascending order


# In[249]:


df[df['Product'].str.match('Mac.*Air')] # Pulling the data that has Mac and Air


# ### Code:
# 
# Write a query to return all of the phone numbers that have an area code of 701 
# (this means the phone numbers begins with 701)

# In[ ]:


import pandas as pd

# Assuming phone_numbers is your DataFrame
# Display the first few rows of the DataFrame

num = phone_numbers[phone_numbers['numbers'].str.startswith('701')]
num


# ## Filtering using Date Functions

# ### These functions are extremely useful to manipulate and use date columns within a Pandas Dataframe. 
# 
# ####  1. "pd.to_datetime( )" function is used to convert an object to a datetime object
# 
# ####  2. ".dt.year" is used to extract the year component from a datetime-like Series
# 
# ####  3. ".dt.day" is used to extract the day component
# 
# ####  4. ".dt.day_name( )" is used to extract the name of the day of the week and is particularly useful when we want to analyze or categorize data based on the day of the week.

# In[186]:


df = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/WeatherHistory.csv')


# In[194]:


pd.set_option('display.max.rows',2500)
pd.set_option('display.max.columns',15)


# In[191]:


df.shape


# In[195]:


df


# In[198]:


df.info() #To check the data type


# In[216]:


df['Formatted Date'] = pd.to_datetime(df['Formatted Date']) # changing datatype of "Formatted Date" column


# In[217]:


df.info()


# In[218]:


df.head()


# In[207]:


df[df['Formatted Date'].dt.year == 2006] # Extracting the data from the year "2006"


# In[219]:


df[df['Formatted Date'].dt.month == 3] # Extracting the data from the month "March"


# In[220]:


df[df['Formatted Date'].dt.day == 26] # Extracting the data from the day "26"


# In[221]:


df[df['Formatted Date'].dt.day_name() == 'Monday'] # Extracting the data that has "Monday"


# ## Filtering using SQL

# In[263]:


df = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/laptop_prices.csv', encoding = 'ISO-8859-1')


# In[264]:


df


# In[272]:


df.query('Price_usd > 2000')


# In[280]:


df.query("Company == 'Apple' or Company == 'Dell'")


# In[281]:


df.query("Company == 'Apple' and Price_usd > 1500")


# In[ ]:





# In[282]:


get_ipython().system('pip install pandasql # pandasql allows us to use SQL syntax to query pandas DataFrames')


# In[283]:


import pandasql as psql


# In[285]:


psql.sqldf("SELECT * FROM df WHERE Company = 'Apple'") # Selecting the data of Apple laptops


# In[308]:


psql.sqldf("SELECT * FROM df WHERE Company = 'Apple' AND Inches > 14") 

# Selecting the data of Apple laptops that has screen size of > 14


# In[309]:


psql.sqldf("SELECT Company, Inches FROM df WHERE Company = 'Apple' AND Inches > 14")

# Extracting Comapany and Inches column by selecting the data of Apple laptops that has screen size of > 14


# In[310]:


df.loc[(df['Company'] == 'Apple') & (df['Inches'] > 14), ['Company', 'Inches']]

# "By Pandas", # Extracting Comapany and Inches column by selecting the data of Apple laptops that has screen size of > 14


# In[311]:


psql.sqldf("SELECT Company, Product FROM df WHERE Product LIKE '%MacBook%'")

# Selecting Company and Product that contain the word 'MacBook' in Product column


# In[312]:


psql.sqldf("SELECT * FROM df ORDER BY Price_usd") # Selecting all columns, sorting by Price in Ascending order


# ## Ordering in DataFrames

# ### ".sort_values( )" method in pandas is used to sort a DataFrame or Series by the values in one or more columns

# In[319]:


df.sort_values(by = 'Price_usd')

# Extracting the data and sorting by price in ascending order


# In[314]:


df.sort_values(by = 'Price_usd', ascending = False)

# Extracting the data and sorting by price in decending order


# In[321]:


df[df['Company'] == 'Lenovo'].sort_values(by = ['Inches','Price_usd'], ascending = [True,False])

# Extracting the data of 'Lenovo' laptops and sorting by screen size and price in ASC, DESC order


# In[ ]:





# ### Code:
# 
# Dr. Obrien has seen an uptick in heart attacks for his patients over the past few months. He has been noticing some trends across his patients and wants to get ahead of things by reaching out to current patients who are at a high risk of a heart attack.
# 
# We need to identify which clients he needs to reach out to and provide that information to Dr. Obrien.
# 
# If a patient is over the age of 50, cholesterol level of 240 or over, and weight 200 or greater, then they are at high risk of having a heart attack.
# 
# Write a query to retrieve these patients. Include all columns in your output.
# 
# As Cholesterol level is the largest indicator, order the output by Cholesterol from Highest to Lowest so he can reach out to them first.

# In[ ]:


high_risk = patients[(patients['age'] > 50) & (patients['cholesterol'] >= 240) & (patients['weight'] >= 200)]

high_risk_final = high_risk.sort_values(by='cholesterol', ascending=False)

high_risk_final


# # Indexing

# #### Indexing in pandas refers to the process of accessing and retrieving data from a DataFrame or Series using labels or positional information.
# 
# #### 1. Use Cases:
# 
# #### - Retrieving specific rows or columns from a DataFrame.
# 
# #### - Selecting individual elements or subsets of data.
# 
# #### - Filtering data based on conditions or criteria.
# 
# #### - Setting and resetting the index to reorganize the data.
# 
# #### - Handling hierarchical or multi-level indexing for complex data structures.
# 
# #### - Facilitating efficient data manipulation and analysis.
# 
# #### 2. Importance:
# 
# #### - Efficient indexing is crucial for quick and accurate data retrieval and manipulation.
# 
# #### - Indexing allows for organized and structured data analysis in pandas.

# ## Creating an Index

# In[367]:


df_World = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/WorldContinents.csv', 
                       encoding = 'ISO-8859-1', index_col = 'country')

# Setting country column as an index


# In[368]:


df_World


# In[354]:


df_Continent = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/WorldContinents.csv', 
                       encoding = 'ISO-8859-1', index_col = 'continent')

# Setting Continent column as an index
df_Continent


# In[355]:


df_World.loc['Albania']


# In[356]:


df_Continent.loc['Asia']


# In[357]:


df


# In[365]:


df.set_index('country', inplace = True)


# In[366]:


df


# In[370]:


df.reset_index(inplace = True)


# In[371]:


df


# ### Multi-Level Indexing

# In[376]:


df.set_index(['continent', 'sub_region']).sort_values(by = ['continent', 'sub_region'])

# Selecting the columns continent and sub_region and sorting them by continent and sub_region


# In[378]:


df.set_index(['continent', 'sub_region']).sort_values(by = ['continent', 'sub_region'], ascending = [False, True])


# ### Filtering on Indexes with .loc and .iloc

# In[379]:


df


# In[381]:


df.set_index(['country'], inplace = True)


# In[382]:


df


# In[386]:


df.loc['Afghanistan']


# In[388]:


df.iloc[1]


# In[389]:


df.reset_index(inplace = True)


# In[390]:


df


# In[391]:


df.set_index(['continent'], inplace = True)


# In[392]:


df


# In[393]:


df.loc['Asia']


# In[394]:


df.iloc[0]


# In[395]:


df.reset_index(inplace = True)


# ### Reordering and Sorting Indexes

# In[404]:


df.set_index(['continent']).sort_index()


# In[406]:


df.set_index(['continent']).sort_index(ascending = False)


# In[415]:


df.set_index(['continent', 'sub_region']).sort_index(level = 'sub_region', ascending = False)


# In[416]:


df.set_index(['continent', 'sub_region']).sort_values(by = ['sub_region'],ascending = False)


# In[430]:


df.set_index(['continent', 'sub_region'], inplace = True)


# In[431]:


df


# In[432]:


df.swaplevel('continent', 'sub_region')


# In[433]:


df.reset_index(inplace = True)


# ### Reshaping and Pivoting Indexes

# In[434]:


df = pd.read_excel('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/tech_price.xlsx')


# In[435]:


df


# In[437]:


df = pd.read_excel('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/tech_price.xlsx'
                   , header = [0,1], index_col = [0,1])


# In[438]:


df


# In[439]:


df.stack()


# In[443]:


df_world = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/WorldContinents.csv', 
                       encoding = 'ISO-8859-1')


# In[444]:


df_world


# In[448]:


df_world.pivot(index = 'country', columns = 'continent', values = 'sub_region')


# In[449]:


df_world.pivot(index = 'country', columns = 'continent', values = 'Unnamed: 4')


# # Group By and Aggregation

# In[454]:


df = pd.read_csv('/Users/akhilnashaboina/Downloads/Pandas for Data Analysis/banking.csv')


# In[457]:


df.shape


# In[472]:


pd.set_option('display.max.rows', 50000)
pd.set_option('display.max.columns', 10)


# In[461]:


df


# In[464]:


df_grouped = df.groupby('marital')


# In[467]:


df_grouped['outstanding_balance'].sum()


# In[470]:


df.groupby('job')['age'].mean()


# In[478]:


pd.set_option('display.max.rows', 50000)
pd.set_option('display.max.columns', 30)


# In[477]:


df.groupby('job').describe()


# ### Code:
# 
# Uncle Ralph's Pizza Shop opened up 5 new stores in 2020. After 3 years Uncle Ralph wanted to see how each of his stores was doing.
# We need to identify which clients he needs to reach out to and provide that information to Dr. Obrien.
# 
# Write a query to determine the average revenue by store.
# 
# Order by revenue largest to smallest.

# In[ ]:


# access datasets as pandas dataframes
import pandas as pd;

#revenue.head()

average_revenue = revenue.groupby('store_id')['revenue_millions'].mean().reset_index()
average_revenue.rename(columns = {'revenue_millions' : 'average_revenue'}, inplace = True)
final = average_revenue.sort_values(by = 'average_revenue', ascending = False)
final


# In[482]:


df.head()


# In[484]:


df.groupby('education')['outstanding_balance'].min()


# In[485]:


df.groupby('education')['outstanding_balance'].max()


# In[488]:


df.groupby('education')['outstanding_balance'].sum().sort_values(ascending = False)


# In[490]:


df.groupby('education')['outstanding_balance'].count().sort_values(ascending = False)


# In[491]:


df.groupby('education')['outstanding_balance'].median().sort_values(ascending = False)


# In[493]:


df.groupby('education').agg({'outstanding_balance' : ['sum', 'count']})


# In[496]:


output = df.groupby('education').agg({'outstanding_balance' : ['sum', 'count']})


# In[499]:


output['average'] = output['outstanding_balance']['sum'] / output['outstanding_balance']['count'] * 100


# In[500]:


output


# In[501]:


df.groupby('education').agg(sum_balance = ('outstanding_balance', 'sum'), count_balance = ('outstanding_balance', 'count'))


# In[ ]:


user_id	session_id	minutes_per_session	activity
1	1	44	Gaming
1	1	27	Homework
1	1	25	YouTube
2	7	37	Gaming
2	6	23	Gaming


# ### Code:
# 
# What was the average time spent, per user, gaming on their computer?

# In[ ]:


# access datasets as pandas dataframes
import pandas as pd;

#sessions.head()
gaming_sessions = sessions[sessions['activity'] == 'Gaming']
gaming = gaming_sessions.groupby('user_id')['minutes_per_session'].mean().reset_index()

gaming.rename(columns = {'minutes_per_session' : 'Average_Time_Gaming'}, inplace = True)

#gaming.columns = ['user_id', 'Average_Time_Gaming']
gaming


# ### Group By on Multiple Columns

# In[503]:


df.shape


# In[506]:


df.head()


# In[504]:


df.groupby(['job', 'marital'])['outstanding_balance'].sum()


# In[507]:


df[df['job'] == 'management'].groupby(['job', 'marital'])['outstanding_balance'].sum()


# In[514]:


df[df['job'] == 'unemployed'].groupby(['job', 'marital'])['outstanding_balance'].sum()


# In[516]:


new_df = df.groupby(['education', 'personal_loan'])['outstanding_balance'].mean()


# In[520]:


final = new_df.reset_index() 


# In[521]:


final


# In[523]:


df.head()


# In[524]:


df.shape


# In[541]:


df_banking = df[:500]


# In[542]:


df_banking['average_balance_per_job'] = df_banking.groupby('job')['outstanding_balance'].transform('mean')


# In[543]:


df_banking


# In[546]:


df_banking['average_balance_per_job'] = df_banking.groupby('job')['outstanding_balance'].transform(lambda x: x-x.mean())


# In[547]:


df_banking


# # Joining DataFrames

# In[ ]:


Merge and the join are somewhat similar. Thw merge uses the columns while the join uses the index.
In general, if we are joining specific columns together or performing different types of joins, Merge is usually the better option.
If we are indexing our columns and we want to join on the index, then that is when we would use Join.


# In[570]:


data1 = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Dwight Schrute', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson'],
    'job_title': ['Regional Manager', 'Sales Representative', 'Receptionist', 'Assistant to the Regional Manager', 'Head of Accounting', 'Accountant', 'Accountant', 'Sales Representative'],
    'salary': [100000, 60000, 55000, 65000, 60000, 55000, 55000, 60000]
}

df1 = pd.DataFrame(data1)


# In[571]:


data2 = {
    'emp_id': [1, 2, 3, 5, 6, 7, 8, 9],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson', 'Phyllis Vance'],
    'department': ['Management', 'Sales', 'Reception', 'Accounting', 'Accounting', 'Accounting', 'Sales', 'Sales']
}

df2 = pd.DataFrame(data2)


# In[572]:


df1


# In[573]:


df2


# In[557]:


df1.merge(df2, how = 'left')


# In[559]:


df1.merge(df2, how = 'right')


# In[560]:


df1.merge(df2, how = 'inner')


# In[561]:


df1.merge(df2, how = 'outer')


# In[566]:


df1.merge(df2, how = 'outer', left_on = 'employee_id', right_on = 'emp_id')


# In[580]:


df1.set_index('employee_id', inplace = True)
df2.set_index('emp_id', inplace = True)


# In[581]:


df1.join(df2, how = 'inner', lsuffix = '_df1', rsuffix = '_df2')


# In[582]:


df1.join(df2, how = 'outer', lsuffix = '_df1', rsuffix = '_df2')


# In[583]:


data1 = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael Scott', 'Creed Bratton', 'Pam Beesly', 'Dwight Schrute', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson'],
    'job_title': ['Regional Manager', 'Sales Representative', 'Receptionist', 'Assistant to the Regional Manager', 'Head of Accounting', 'Accountant', 'Accountant', 'Sales Representative'],
    'salary': [100000, 60000, 55000, 65000, 60000, 55000, 55000, 60000]
}

df1 = pd.DataFrame(data1)


# In[584]:


data2 = {
    'employee_id': [1, 2, 3, 5, 6, 7, 8, 9],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson', 'Phyllis Vance'],
    'department': ['Management', 'Sales', 'Reception', 'Accounting', 'Accounting', 'Accounting', 'Sales', 'Sales']
}

df2 = pd.DataFrame(data2)


# In[585]:


df1


# In[586]:


df2


# In[590]:


pd.merge(df1, df2, on = 'employee_id', how = 'inner')


# In[592]:


pd.merge(df1[['employee_id', 'job_title']], df2[['employee_id', 'department']], on = 'employee_id', how = 'inner')


# In[595]:


pd.merge(df1, df2, on = 'employee_id', how = 'inner', suffixes = ('_left', '_right'))


# In[597]:


pd.merge(df1, df2, on = 'employee_id', how = 'outer', suffixes = ('_left', '_right'), indicator = True)


# ### Merging Multiple DataFrames

# In[598]:


import pandas as pd

data1 = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Dwight Schrute', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson'],
    'job_title': ['Regional Manager', 'Sales Representative', 'Receptionist', 'Assistant to the Regional Manager', 'Head of Accounting', 'Accountant', 'Accountant', 'Sales Representative'],
    'salary': [100000, 60000, 55000, 65000, 60000, 55000, 55000, 60000]
}

demographics = pd.DataFrame(data1)

data2 = {
    'employee_id': [1, 2, 3, 5, 6, 7, 8, 9],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson', 'Phyllis Vance'],
    'department_id': [1, 2, 3, 4, 4, 4, 2, 2]
}

name_dep = pd.DataFrame(data2)


data3 = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'manager_id': [None, 1, 1, 1, 1, 4, 4, 1, 1]
}


manager = pd.DataFrame(data3)


data4 = {
    'department_id': [1, 2, 3, 4],
    'department': ['Management', 'Sales', 'Reception', 'Accounting']
}


department = pd.DataFrame(data4)


# In[602]:


manager['manager_id'] = manager['manager_id'].astype('Int64')


# In[603]:


manager


# In[600]:


department


# In[604]:


name_dep


# In[605]:


demographics


# In[608]:


pd.merge(demographics, name_dep, on = 'employee_id', how = 'inner').merge(department, on = 'department_id', how = 'inner')


# In[610]:


pd.merge(demographics, name_dep, on = 'employee_id', how = 'inner').merge(department, on = 'department_id', how = 'inner').merge(manager, on = 'employee_id', how = 'inner')


# ### Concatenation

# In[606]:


import pandas as pd

data1 = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Dwight Schrute', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson'],
    'job_title': ['Regional Manager', 'Sales Representative', 'Receptionist', 'Assistant to the Regional Manager', 'Head of Accounting', 'Accountant', 'Accountant', 'Sales Representative'],
    'salary': [100000, 60000, 55000, 65000, 60000, 55000, 55000, 60000]
}

df1 = pd.DataFrame(data1)

data2 = {
    'employee_id': [1, 2, 3, 5, 6, 7, 8, 9],
    'name': ['Michael Scott', 'Jim Halpert', 'Pam Beesly', 'Angela Martin', 'Kevin Malone', 'Oscar Martinez', 'Stanley Hudson', 'Phyllis Vance'],
    'department': ['Management', 'Sales', 'Reception', 'Accounting', 'Accounting', 'Accounting', 'Sales', 'Sales']
}

df2 = pd.DataFrame(data2)


# In[611]:


df1


# ## 

# In[612]:


df2


# In[617]:


pd.concat([df1, df2])


# In[620]:


pd.concat([df1, df2], axis = 1)


# In[619]:


pd.concat([df1, df2], axis = 1, join = 'inner')


# In[621]:


pd.concat([df1.set_index('employee_id'), df2.set_index('employee_id')], axis = 1, join = 'inner')


# In[622]:


pd.concat([df1, df2], axis = 0)


# In[626]:


pd.concat([df1[['employee_id', 'name']], df2[['employee_id', 'name']]], axis = 0).drop_duplicates().reset_index().drop('index', axis = 1)


# In[629]:


pd.concat([df1, df2], axis = 0, ignore_index = True)


# In[631]:


pd.concat([df1, df2], axis = 0,keys = ['DF1', 'DF2'])


# In[ ]:




