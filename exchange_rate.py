import requests
import json

def get_exchange_rates():
    """
    Fetches current exchange rates from USD to various currencies
    """
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        print("Fetching exchange rates...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        print("\n=== EXCHANGE RATES (USD BASE) ===")
        print(f"Last updated: {data['date']}")
        print("\nPopular currencies:")
        print("-" * 25)
        
        currencies = ['EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'INR']
        for currency in currencies:
            if currency in data['rates']:
                print(f"{currency}: {data['rates'][currency]:.4f}")
                
        return data
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    get_exchange_rates()
