# By: Danyal Khattak

#%%

### Data Cleaning: Part - a

import pandas as pd

# Column names from description
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 
                'DIS', 'RAD', 'TAX', 'PTRATIO', 'LSTAT', 'MEDV']

# Loading the CSV file, specifying no header and assigning column names
bh = pd.read_csv('E:\\Surrey MSc reading list\\Semester 1\\Principles of Data Science\\Midterm\\boston_housing_mid.csv', header=None, names=column_names)

# Displaying the top 5 lines 
print(bh.head())

# Displaying the number of rows and columns
print("Number of rows:", bh.shape[0])
print("Number of columns:", bh.shape[1])

#%%
### Data Cleaning: Part - b

print(bh.dtypes)
bh['RAD'] = bh['RAD'].astype('float64')
bh['CHAS'] = bh['CHAS'].astype('bool')

print(bh.dtypes)

#%%
### Data Cleeaning: Part - c

# Identifying missing values and their counts
missing_values_count = bh.isna().sum()

# Displaying only attributes with missing values
print(missing_values_count[missing_values_count > 0])

# Making copies of the dataset for each of the method for removing the null values. 
bh_del_col = bh.copy()
bh_del_row = bh.copy()
bh_null_0 = bh.copy()
bh_null_ffill = bh.copy()

# 1. Dropping each column with a null value
bh_del_col.dropna(axis=1, inplace=True)
print(bh_del_col)
bh_del_col.info()


# 2. Dropping each row with a null value.
bh_del_row.dropna(inplace=True)
print(bh_del_row)
bh_del_row.info()


# 3. Replacing null values with 0.
bh_null_0.fillna(0, inplace=True)
print(bh_null_0)
bh_null_0.info()

# 4. Writing a function that replaces the null values with mean of 2 rows above and below the null value.  
bh_null_ffill['NOX'].fillna(method='ffill', inplace=True)
print(bh_null_ffill[['NOX']])  
bh_null_ffill.info()


#%%
### Preparation for analysis: Part - a

## (I)
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
# 1. Creating the 'NOX_cat' 
bh['NOX_cat'] = pd.cut(bh_null_ffill['NOX'], bins=9, labels=range(1, 10))

# 2. Using Stratified Shuffle Split on 'NOX_cat'
split = StratifiedShuffleSplit(n_splits=1, test_size=0.22, random_state=42) 
for train_index, test_index in split.split(bh, bh['NOX_cat']):
    bh_train_set = bh.loc[train_index]
    bh_test_set = bh.loc[test_index]
    

## (II)
import pandas as pd
import matplotlib.pyplot as plt

# Creating histograms
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
bh['NOX_cat'].hist(bins=9) 
plt.title('Original Dataset')

plt.subplot(1, 2, 2)
bh_test_set['NOX_cat'].hist(bins=9) 
plt.title('Stratified Test Set')

plt.suptitle("NOX_cat Distribution")
plt.tight_layout() 
plt.show()


## (III)

# Proportions in the training set
train_proportions = bh_train_set['NOX_cat'].value_counts() / len(bh_train_set)

# Proportions in the Original set
test_proportions = bh_test_set['NOX_cat'].value_counts() / len(bh_test_set)

# Printing for comparison
print("Training Set Proportions:\n", train_proportions)
print("Test Set Proportions:\n", test_proportions)


## (IV)

# Removing 'NOX_cat' column
for set_ in (bh, bh_train_set, bh_test_set): 
    set_.drop("NOX_cat", axis=1, inplace=True)

# Printing shapes
print("Shape of Training Set:", bh_train_set.shape)
print("Shape of Test Set:", bh_test_set.shape)
print("Shape of Original Dataset:", bh.shape)

# Calculating the ratio of the length of the test set to that of the original
test_set_ratio = len(bh_test_set) / len(bh) * 100
print("Test Set Ratio:", test_set_ratio, "%") 


#%%
### Data Analysis



## (I)
correlation_matrix = bh_train_set.corr()
print(correlation_matrix)



## (II)
# Calculating correlations with 'MEDV'
correlation_medv = bh_train_set.corr()['MEDV']

# Sorting in descending order
MEDV_sorted_correlations = correlation_medv.sort_values(ascending=False)

print(MEDV_sorted_correlations)



## (III)
MEDV_Scatter = ['MEDV', 'INDUS', 'NOX','LSTAT','RM']

# Creating the scatter matrix for MEDV, INDUS, NOX, LSTAT, and RM
pd.plotting.scatter_matrix(bh[MEDV_Scatter], figsize=(10, 10))
plt.show()



## (IV)
AGE_Scatter = ['MEDV', 'AGE']

# Creating the scatter matrix for MEDV vs AGE
pd.plotting.scatter_matrix(bh[AGE_Scatter], figsize=(10, 10))
plt.show()



## (IV)
AGE_RM_Scatter = ['RM', 'AGE']

# Creating the scatter matrix for RM and AGE
pd.plotting.scatter_matrix(bh[AGE_RM_Scatter], figsize=(10, 10))
plt.show()


