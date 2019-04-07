from django.shortcuts import render
from datetime import datetime
import sys
from .services import *

def validate_date_range(d_from, d_to):
    days_diff = (datetime.fromisoformat(d_to) - datetime.fromisoformat(d_from)).days
    if (days_diff < 0):
        return "To date must be after from date"
    elif (days_diff > 31):
        return "Range of records limited to a month - please refine your date range"
    return None

# Create your views here.
def index(request):
    ticker = request.POST.get('ticker','').upper()
    d_from = request.POST.get('d_from','')
    d_to = request.POST.get('d_to','')

    retrieved_stock_data_record_count = 0
    retrieved_stock_data = None
    result_code = None
    validation_message = None
    error_message = None

    if ticker and d_from:
        if d_from and d_to:
            validation_message = validate_date_range(d_from, d_to)
        if not validation_message:
            try:
                (result_code, retrieved_stock_data) = \
                    invoke_trajan_service(ticker, d_from, d_to)
            except:
                print(sys.exc_info())
                error_message = sys.exc_info()
    elif request.method == 'POST':
        validation_message = (
            "You must provide at least a stock code and"
            "a from date to search for historical records")

    if retrieved_stock_data:
        retrieved_stock_data_record_count = len(retrieved_stock_data)

    return render(request, 'trajan/index.html',
                  {'ticker': ticker,
                   'd_from': d_from,
                   'd_to': d_to,
                   'stock_data': retrieved_stock_data,
                   'stock_data_record_count': retrieved_stock_data_record_count,
                   'result_code': result_code,
                   'validation_message': validation_message,
                   'error_message': error_message})
