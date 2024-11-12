from django.shortcuts import render
from .models import Stock
from .utils import get_stock_data

def stock_list(request):
    stocks = Stock.objects.all()  # Fetch all stocks from the database
    return render(request, 'analysis/stock_list.html', {'stocks': stocks})

def update_stock_data(request):
    # Example of updating stock data
    symbols = ['AAPL', 'GOOGL', 'MSFT']  # List of stock symbols to update
    for symbol in symbols:
        stock_data = get_stock_data(symbol)
        stock, created = Stock.objects.update_or_create(
            symbol=stock_data['symbol'],
            defaults={
                'last_price': stock_data['current_price'],
                'timestamp': stock_data['timestamp'],
            }
        )
    return render(request, 'analysis/stock_list.html', {'stocks': Stock.objects.all()})