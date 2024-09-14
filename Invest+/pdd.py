import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Optional: Set up for displaying Chinese characters (if needed)
# plt.rcParams['font.sans-serif'] = ['SimHei']  # For displaying Chinese labels
# plt.rcParams['axes.unicode_minus'] = False    # For displaying negative signs correctly

# Get Pinduoduo's stock data
ticker = 'PDD'
pdd = yf.Ticker(ticker)

# Get financial statements
income_statement = pdd.financials    # Income statement
balance_sheet = pdd.balance_sheet    # Balance sheet
cash_flow = pdd.cashflow             # Cash flow statement

# Transpose data for easier handling
income_statement = income_statement.T
balance_sheet = balance_sheet.T
cash_flow = cash_flow.T

# Reset index for plotting
income_statement.reset_index(inplace=True)
balance_sheet.reset_index(inplace=True)
cash_flow.reset_index(inplace=True)

# Format the dates
income_statement['index'] = pd.to_datetime(income_statement['index'])
balance_sheet['index'] = pd.to_datetime(balance_sheet['index'])
cash_flow['index'] = pd.to_datetime(cash_flow['index'])

# Plot total revenue trend
plt.figure(figsize=(10,6))
plt.plot(income_statement['index'], income_statement['Total Revenue'] / 1e9, marker='o')
plt.title('Pinduoduo Total Revenue Trend (USD Billions)')
plt.xlabel('Date')
plt.ylabel('Total Revenue (USD Billions)')
plt.grid(True)
plt.show()

# Plot net income trend
plt.figure(figsize=(10,6))
plt.plot(income_statement['index'], income_statement['Net Income'] / 1e9, marker='o', color='green')
plt.title('Pinduoduo Net Income Trend (USD Billions)')
plt.xlabel('Date')
plt.ylabel('Net Income (USD Billions)')
plt.grid(True)
plt.show()

# Plot operating cash flow trend
plt.figure(figsize=(10,6))
plt.plot(cash_flow['index'], cash_flow['Total Cash From Operating Activities'] / 1e9, marker='o', color='orange')
plt.title('Pinduoduo Operating Cash Flow Trend (USD Billions)')
plt.xlabel('Date')
plt.ylabel('Operating Cash Flow (USD Billions)')
plt.grid(True)
plt.show()

# Plot total assets vs. total liabilities
plt.figure(figsize=(10,6))
plt.plot(balance_sheet['index'], balance_sheet['Total Assets'] / 1e9, marker='o', label='Total Assets')
plt.plot(balance_sheet['index'], balance_sheet['Total Liab'] / 1e9, marker='o', label='Total Liabilities')
plt.title('Pinduoduo Total Assets vs. Total Liabilities (USD Billions)')
plt.xlabel('Date')
plt.ylabel('Amount (USD Billions)')
plt.legend()
plt.grid(True)
plt.show()
