# Trading Performance Metrics

This repository contains a Python script that calculates two key performance metrics from a trade log:

- **Profit Factor** = total profit / total loss (ignoring signs).  
- **Sharpe Ratio** (annualized) = mean daily P&L / standard deviation of daily P&L × sqrt(252).

## Files
- `performance.py` – script to compute metrics.
- `Trading Journal - Trades.csv` – example trade log (your own data).

## How to use
1. Install pandas: `pip install pandas`
2. Place your CSV in the same folder as `performance.py`.  
   The CSV must have a column named exactly `'P&L $'` (adjust if yours differs).
3. Run: `python performance.py`

## Example output
q!
:q!

