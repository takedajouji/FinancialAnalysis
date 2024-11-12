import symbol

import requests
import os

def get_stock_data(symnol):
    api_key = os.getenv'<KEY>' #finnhub API key
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    data = response.json()
    return {
        'symbol': symbol,
        'current_price': data['c'],
        'high_price': data['h'],
        'low_price': data['l'],
        'open_price': data['o'],
        'previous_close': data['pc'],
        'timestamp': data['ts'],
    }