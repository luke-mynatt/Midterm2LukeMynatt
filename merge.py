import pandas as pd

# Load the CSV files
unrate_df = pd.read_csv('UNRATE.csv')
cpi_df = pd.read_csv('CPIAUCSL.csv')
gdp_df = pd.read_csv('GDP.csv')

# Merge the DataFrames on the 'DATE' column
merged_df = pd.merge(unrate_df, cpi_df, on='DATE', how='outer')
merged_df = pd.merge(merged_df, gdp_df, on='DATE', how='outer')

# Fill missing values with the column mean
# Note: Adjust the warning suppression based on the version of pandas
merged_df_filled = merged_df.fillna(merged_df.mean(numeric_only=True))

# Optionally, save the merged DataFrame to a new CSV file
merged_df_filled.to_csv('./merged_output.csv', index=False)

# Display the merged DataFrame
print(merged_df_filled.head())
