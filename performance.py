import pandas as pd

df = pd.read_csv('Trading Journal - Trades.csv')

# Use the exact column name
profits = df[df['P&L $'] > 0]['P&L $'].sum()
losses = df[df['P&L $'] < 0]['P&L $'].sum()
profit_factor = profits / abs(losses) if losses != 0 else float('inf')

returns = df['P&L $'] / 1000   # adjust scaling if needed
sharpe = returns.mean() / returns.std() * (252 ** 0.5)

print(f"Profit Factor: {profit_factor:.2f}")
print(f"Sharpe Ratio: {sharpe:.2f}")
