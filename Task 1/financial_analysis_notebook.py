# -*- coding: utf-8 -*-
"""Financial_Analysis_Notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wnBJBV-IbE8F4annuppXpzdUTaz5TzWU
"""

# Import necessary libraries
import pandas as pd

# Load the data from CSV file
# Replace 'financial_data.csv' with the path to your actual CSV file
df = pd.read_csv('financial_data.csv')

# Display the first few rows of the dataset to check the data
print("Data Preview:")
print(df.head())

# Calculate year-over-year growth percentages for key financial metrics
df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100
df['Assets Growth (%)'] = df.groupby('Company')['Total Assets'].pct_change() * 100
df['Liabilities Growth (%)'] = df.groupby('Company')['Total Liabilities'].pct_change() * 100
df['Cash Flow Growth (%)'] = df.groupby('Company')['Cash Flow from Operating Activities'].pct_change() * 100

# Calculate Debt-to-Asset Ratio
df['Debt-to-Asset Ratio'] = df['Total Liabilities'] / df['Total Assets'] * 100

# Display summary of calculated columns
print("\nData with Calculated Growth and Ratios:")
print(df[['Company', 'Year', 'Revenue Growth (%)', 'Net Income Growth (%)',
         'Assets Growth (%)', 'Liabilities Growth (%)', 'Cash Flow Growth (%)',
         'Debt-to-Asset Ratio']])

# Aggregate average growth rate for each company
summary_df = df.groupby('Company').agg({
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean',
    'Assets Growth (%)': 'mean',
    'Liabilities Growth (%)': 'mean',
    'Cash Flow Growth (%)': 'mean',
    'Debt-to-Asset Ratio': 'mean'
}).reset_index()

# Rename columns for clarity in summary
summary_df.columns = ['Company', 'Avg Revenue Growth (%)', 'Avg Net Income Growth (%)',
                      'Avg Assets Growth (%)', 'Avg Liabilities Growth (%)',
                      'Avg Cash Flow Growth (%)', 'Avg Debt-to-Asset Ratio']

# Display the summary table
print("\nSummary of Average Growth and Ratios by Company:")
print(summary_df)

# Export analysis to CSV for reference
# Replace 'financial_analysis_summary.csv' with your preferred filename
summary_df.to_csv('financial_analysis_summary.csv', index=False)
print("\nSummary exported to 'financial_analysis_summary.csv'.")

# Observations Summary
observations = """
### Financial Analysis Observations:
1. Microsoft:
   - Shows stable growth in revenue and net income over the last three years.
   - Maintains a healthy Debt-to-Asset Ratio.

2. Tesla:
   - Exhibits high revenue growth due to expansion efforts, with variability in net income.

3. Apple:
   - Demonstrates consistent revenue growth and strong cash flow, maintaining a relatively low debt-to-asset ratio.
"""
print("\nObservations Summary:")
print(observations)