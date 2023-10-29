import pandas as pd
import matplotlib.pyplot as plt


file_path = "C:/Users/Legion/Desktop/archive/Billionaires Statistics Dataset.csv"
data = pd.read_csv(file_path)

print(data.head())
print(data.info())


# Counting the number of duplicates
dublicate_count = data.duplicated().sum()
print(f'Dublicates: {dublicate_count}')


# Counting missing values in each column
missing_values = data.isnull().sum()
print('Missing values in each column:')
print(missing_values)


# Delete columns with missing values
colums_to_drop = ['organization', 'title', 'state', 'residenceStateRegion']
data = data.drop(columns=colums_to_drop)
# Output of updated data
print(data.head())


# Descriptive statistics
numeric_stats = data.describe()
print(numeric_stats)

# Analysis of categorical variables
category_counts = data['category'].value_counts()
source_counts = data['source'].value_counts()
gender_counts = data['gender'].value_counts()
print('Category:')
print(category_counts)
print(category_counts.head())
print('Source:')
print(source_counts)
print('Gender:')
print(gender_counts)


# Age histogram
plt.hist(data['age'], bins=20)
plt.title("Age distribution of the richest people")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Wealth histogram
plt.hist(data['finalWorth'], bins=20, color='skyblue')
plt.xlabel('Wealth')
plt.ylabel('Number of richest')
plt.title('Distribution of wealth among the richest people')
plt.show()

# Statistical indicators
mean_wealth = data['finalWorth'].mean()
median_wealth = data['finalWorth'].median()
std_wealth = data['finalWorth'].std()
print(f'Average wealth: {mean_wealth}')
print(f'Median wealth: {median_wealth}')
print(f'Standard deviation of wealth: {std_wealth}')


# Average age
mean_age = data['age'].mean()
print(f'Average age of the richest: {mean_age}')

# Top categories
print('Top category:')
print(category_counts.head())


# Segmentation by source of wealth
wealth_sources = data.groupby('source')
source_statistics = wealth_sources['finalWorth'].agg(['mean', 'median', 'count'])
print(source_statistics)


# Country segmentation
countries = data.groupby('country')
country_statistics = countries['finalWorth'].agg(['mean', 'median', 'count'])
print(country_statistics)

# Segment visualization
source_statistics.plot(kind='bar', y='mean', figsize=(10, 6), title='Average wealth by source')
plt.ylabel('Average wealth')
plt.show()
