#DataCleaning

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('avocado.csv')

# Drop the column you don't need
df = df.drop(['4046', '4225', '4770', 'Unnamed: 0'], axis=1)

df = df.sort_values('Date', ascending=True).reset_index(drop=True)
df = df[df['type'] == 'organic']

df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

# Write the modified DataFrame back to a CSV file
df.to_csv('avocado_clean1.csv', index=False)
