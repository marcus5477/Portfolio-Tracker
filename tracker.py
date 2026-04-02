#!/usr/bin/env python3
"""
Professional Portfolio Tracker
Fetches real-time exchange rates and logs them to CSV
"""

import requests
import csv
import argparse
from datetime import datetime
import sys

def fetch_exchange_rates(currencies):
    """
    Fetch current exchange rates from API
    """
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        print("Fetching exchange rates...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Validate currency codes
        valid_currencies = {}
        invalid_currencies = []
        
        for currency in currencies:
            if currency.upper() in data['rates']:
                valid_currencies[currency.upper()] = data['rates'][currency.upper()]
            else:
                invalid_currencies.append(currency.upper())
        
        return {
            'valid_rates': valid_currencies,
            'invalid_currencies': invalid_currencies,
            'timestamp': data['date'],
            'base_currency': data['base']
        }
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed. Please check your internet.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def log_to_csv(rates_data, filename='portfolio_history.csv'):
    """
    Log rates and timestamp to CSV file
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Check if file exists
        file_exists = False
        try:
            with open(filename, 'r') as f:
                file_exists = True
        except FileNotFoundError:
            file_exists = False
        
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write headers if file doesn't exist
            if not file_exists:
                writer.writerow(['timestamp', 'base_currency', 'target_currency', 'exchange_rate', 'api_timestamp'])
            
            # Write each rate
            for currency, rate in rates_data['valid_rates'].items():
                writer.writerow([timestamp, rates_data['base_currency'], currency, rate, rates_data['timestamp']])
                
        print(f"Data logged to {filename}")
        return True
        
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        return False

def display_rates(rates_data):
    """
    Display formatted exchange rates
    """
    if not rates_data or not rates_data['valid_rates']:
        print("No valid rates to display")
        return
    
    print(f"\nPORTFOLIO TRACKER RESULTS")
    print("=" * 50)
    print(f"Base Currency: {rates_data['base_currency']}")
    print(f"API Data Date: {rates_data['timestamp']}")
    print(f"Fetched at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Display valid rates
    print("VALID CURRENCIES:")
    for currency, rate in rates_data['valid_rates'].items():
        print(f"   {currency}: {rate:.4f}")
    
    # Display invalid currencies
    if rates_data['invalid_currencies']:
        print("\nINVALID CURRENCY CODES (ignored):")
        for currency in rates_data['invalid_currencies']:
            print(f"   {currency}")

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description='Professional Portfolio Tracker - Fetch and log currency exchange rates',
        epilog='Example: python tracker.py GBP EUR JPY'
    )
    
    parser.add_argument(
        'currencies',
        nargs='+',
        help='Currency codes to track (e.g. GBP EUR JPY CAD)'
    )
    
    args = parser.parse_args()
    
    # Validate we have at least one currency
    if not args.currencies:
        print("Please provide at least one currency code to track")
        parser.print_help()
        sys.exit(1)
    
    print(f"Tracking {len(args.currencies)} currencies: {', '.join(args.currencies)}")
    
    # Fetch rates
    rates_data = fetch_exchange_rates(args.currencies)
    
    if rates_data:
        # Display results
        display_rates(rates_data)
        
        # Log to CSV
        if rates_data['valid_rates']:
            log_to_csv(rates_data)
        else:
            print("No valid rates to log to CSV")
    else:
        print("Failed to fetch exchange rates.")

if __name__ == "__main__":
    main()
