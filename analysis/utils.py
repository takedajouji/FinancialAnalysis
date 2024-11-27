import symbol
import requests
import os


def get_stock_data(symbol):
    api_key = os.getenv('KEY')  # Finnhub API key
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        return {
            'symbol': symbol,
            'current_price': data.get('c'),
            'high_price': data.get('h'),
            'low_price': data.get('l'),
            'open_price': data.get('o'),
            'previous_close': data.get('pc'),
            'timestamp': data.get('ts'),
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return None