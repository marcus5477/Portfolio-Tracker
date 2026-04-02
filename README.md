<<<<<<< HEAD
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

=======
# Portfolio-Tracker

A professional CLI tool for tracking real-time currency exchange rates with histroical CSV logging.

## ♦️ features 

- **real time API integration** : fetches live exchange rates from ExchangeRate-API
- **CSV Data Logging** :  maintains a historical portoflio data of pulled exchange rates 'portfolio_history.csv'
- **Error Resilience** : graceful handling of numrerous erros (network, invalid inputs, API slow/failures)
- **proffessional CLI** : AI backtasted for clean line interface and informative feedback
- **portfolio managment** : ability for multiple curriences to be tracked through a single command ( GBP EUR JPY)

  ## 🚀 Quick Start
  ```bash
# Clone and run in 30 seconds
git clone https://github.com/marcus5477/Portfolio-Tracker.git
cd Portfolio-Tracker
pip install -r requirements.txt
python tracker.py GBP EUR JPY

Install dependencies 
pip install -r requirements.txt

Verify Installation 
python tracker.py --help

## 💱 example run through

python tracker.py GBP EUR JPY CAD AUD CNY

Tracking 3 currencies: GBP, EUR, JPY
Fetching exchange rates...

PORTFOLIO TRACKER RESULTS
==================================================
Base Currency: USD
API Data Date: 2025-11-21
Fetched at: 2025-11-21 15:30:45
--------------------------------------------------
VALID CURRENCIES:
   GBP: 0.7640
   EUR: 0.8660
   JPY: 156.6300
Data logged to portfolio_history.csv

## 🛠️ Technologies

- **Python 3.13** - Core programming language
- **Requests** - HTTP library for API calls
- **CSV Module** - Data persistence and logging
- **argparse** - Professional command-line interface
- **datetime** - Precise timestamping

## 🛡️ Error Handling

The tool gracefully handles:
- **Network issues**: Timeouts, connection failures
- **Invalid inputs**: Non-existent currency codes
- **API limitations**: Rate limits, service outages
- **File issues**: Permission errors, locked files

Example error message: ' request timed out. please check your internet connection. '
>>>>>>> 4e7fb269e81bd933b25d6366c343c60e172bf338
