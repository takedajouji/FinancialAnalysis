from django.urls import path
from .views import stock_list, update_stock_data

urlpatterns = [
    path('', stock_list, name='stock_list'),
    path('update/', update_stock_data, name='update_stock_data'),
]
