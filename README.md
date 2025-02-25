# Boston-Housing
Analyzed the correlations between housing variables and median home value in Boston, MI.

This was a small project I did on finding correlations between different variables and the median home value in Boston. 

The dataset used is open-source and can be found easily online. 

There were a total of 13 variables that alluded to various characteristics of housing units in the Boston Areas, qualities like number of rooms, proximity to the sea, etc.

# Data Cleaning
I used the print(bh.dtypes) command to show the types of variables that were being used in the dataset. The RAD and CHAS variables were not in the type specified and were converted to the float64 and bool data type using the astype command.

In order to find the variables where the missing values were in and how many there were, I created the list using the bh.isna().sum() command. The output below shows that the variable “NOX” had 9 missing values.

I used the various methods for filling or replacing all the null values found in the NOX column. Initially, I made copies of the dataset using the bh.copy command, followed by the following four commands for all the tasks i to iv.
bh_del_col.dropna(axis=1, inplace=True)
bh_del_row.dropna(inplace=True)
bh_null_0.fillna(0, inplace=True)
bh_null_ffill['NOX'].fillna(method='ffill', inplace=True)

Finally, I decided on using the ffill command to fill in the null values, because by looking at the data for NOX, I realized that while the values for the individual entries were continuous (0.538, 0.469, 0.573), there were vast regions of the dataset with the same recurring value (e.g. columns 13 to 34 had the value 0.538 for the NOX variable, and the pattern repeated throughout the dataset). This led to the logical conclusion that there was a very high chance that the missing values would be the same as those above and below it, hence using the ffill method would maximize the probability
of
replacing the null value with the correct one. On the other hand, if the mean or median of the whole column were used, it would have resulted in values that did not conform to the pattern of the data.


# Data Analysis
## Splitting the data into training and test sets for further analysis
The code creates a categorical feature named "NOX_cat" from the existing numerical "NOX" feature in the "bh_null_ffill" data frame. Then, it splits the "bh" data frame using a stratified shuffle split with "NOX_cat" as the base for stratification. The split divides the data into a 22% testing set and a 78% training set. The indices for training and testing sets are separated and assigned to new data frames named "bh_train_set" and "bh_test_set".

The code first binned the continuous 'NOX' data into a categorical feature called 'NOX_cat'. Then, it used a stratified shuffle split to divide the dataset into training and testing sets, ensuring that the distribution of 'NOX_cat' remained similar across both splits. To visualize the success of this stratification, histograms were generated for 'NOX_cat' in both the original dataset and the test set. The output showed very similar histograms, demonstrating that the stratified sampling effectively maintained the 'NOX' variable's distribution within the testing set.

As shown from the outputs, the proportions are fairly close for each 'NOX_cat' category between the original data and the test set. This confirms that the stratified shuffle split did a good job of maintaining the distribution of the 'NOX' variable.

The .shape command was used to show the dimensions of the original, test and train sets. And the test set ratio (length of test set to the original set) was calculated using the following formula:

test_set_ratio = len(bh_test_set) / len(bh) * 100

The code successfully split the original dataset (506 data points) into a training set (394 points) and a testing set (112 points). The training and testing sets have 13 columns each, indicating they contain the same features as the original dataset, minus the removed 'NOX_cat' column. The split achieved a test set ratio of 22.13%, closely aligning with the intended 22% split. This demonstrates that the stratified shuffle split effectively divided the data while preserving the distribution of the 'NOX' feature (or whichever feature was used for stratification). The outputs for the code were:

Shape of Training Set: (394, 13)
Shape of Test Set: (112, 13)
Shape of Original Dataset: (506, 13)
Test Set Ratio: 22.1343 %


## Correlation Matrix of variables
This analysis was generated using a simple code snippet. The core calculation is bh_train_set.corr(), which computes the pairwise correlations between all numerical columns in the 'bh_train_set' DataFrame. The resulting correlation matrix was then printed for review

The correlation matrix highlights the relationships between the median value of homes ('MEDV') and other housing attributes.

Notably, the number of rooms ('RM') shows the strongest positive correlation with 'MEDV', logically suggesting larger homes tend to have higher prices.

Conversely, the percentage of lower status population ('LSTAT') shows the strongest negative correlation. This implies that areas with higher 'LSTAT' tend to have lower median home values, implying that homes found in neighborhoods with a population of a lower social status are generally cheaper than similar homes in other regions.

Interestingly, factors such as the age of the house “AGE” or the, all important, seaside location of the home, do not make for substantial changes in the price of a home.

The high correlation of the median value with the pupil teacher ratio is also an interesting occurrence. It implies that as the quality of education decreases, the median value of houses in that region decreases, this also ties in with the correlation established with the LSTAT variable.

Other factors like crime rate ('CRIM'), industry ('INDUS'), and property tax ('TAX') also exhibit negative correlations with 'MEDV'.

## Visualizing the Results
The scatter matrix output shows the two most highly correlated variables (LSTAT and RM) along INDUS and NOX with MEDV.

The connection between the industrial factor and median value seems to be more of a binary variable, where most of the industrial zones are generally found in low value housing regions, as shown by the sharp decline in the number of industrial zones after the value of house goes above ~28.

There also seems to be a substantial correlation between the Nitrous oxide concentration and the number of industrial units in the region, which also makes sense as it is these regions where that gas is generally generated. I believe this is the other correlation that was mentioned in the assignment.

The number of rooms per household and the status of the population seems to be mildly inversely proportional to each other, this also follows from reason that neighborhoods that are generally not that well off will have smaller housing units.

# Results
The relationship between the Age variable and median value of a home does not seem to be a strong one. While some pattern does emerge, which shows that generally, houses that are older have a lower median value but above a specific point (around a median value of ~17(hundred thousand?) age does not play an important role in determining the median value.

Interestingly, there seems to be quite a few outliers, in this case. In the top-right plot in the first scatter graph, there is a concentration of houses that have a high median value and are generally quite old (close to 100).

While there is no exact positive or negative relationship between the number of rooms and the age of a house, a quick visual inspection shows that some patterns do emerge.

Firstly, it is shown houses that are built more recently, generally tend to have between 5 and 8 rooms. However homes that are built before 1940 have quite a substantial number that have fewer rooms, as shown by the overcrowded right side of scatter plot in the top right of the second plot.


