import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the uploaded CSV files
gdp_canada = pd.read_csv('./NGDPRSAXDCCAQ.csv')
gdp_usa = pd.read_csv('./GDPC1.csv')

# Convert DATE columns to datetime format for both datasets
gdp_canada['DATE'] = pd.to_datetime(gdp_canada['DATE'])
gdp_usa['DATE'] = pd.to_datetime(gdp_usa['DATE'])

# Filter data for the last decade
last_decade = pd.Timestamp('2013-01-01')
gdp_canada_last_decade = gdp_canada[gdp_canada['DATE'] >= last_decade]
gdp_usa_last_decade = gdp_usa[gdp_usa['DATE'] >= last_decade]

# Calculate GDP growth rates
gdp_canada_last_decade['Growth Rate'] = gdp_canada_last_decade['NGDPRSAXDCCAQ'].pct_change() * 100
gdp_usa_last_decade['Growth Rate'] = gdp_usa_last_decade['GDPC1'].pct_change() * 100

# Creating a line plot of GDP growth rates
plt.figure(figsize=(12, 6))
sns.lineplot(x='DATE', y='Growth Rate', data=gdp_canada_last_decade, label='Canada GDP Growth')
sns.lineplot(x='DATE', y='Growth Rate', data=gdp_usa_last_decade, label='USA GDP Growth')
plt.title('GDP Growth Over the Last Decade for Canada and USA')
plt.xlabel('Date')
plt.ylabel('GDP Growth Rate (%)')
plt.legend()
plt.grid(True)
plt.show()


# Calculate mean, median, and standard deviation for both datasets
stats_canada = {
    "Mean": gdp_canada_last_decade['Growth Rate'].mean(),
    "Median": gdp_canada_last_decade['Growth Rate'].median(),
    "Standard Deviation": gdp_canada_last_decade['Growth Rate'].std()
}

stats_usa = {
    "Mean": gdp_usa_last_decade['Growth Rate'].mean(),
    "Median": gdp_usa_last_decade['Growth Rate'].median(),
    "Standard Deviation": gdp_usa_last_decade['Growth Rate'].std()
}

print("Statistics for Canada:", stats_canada)
print("Statistics for USA:", stats_usa)
