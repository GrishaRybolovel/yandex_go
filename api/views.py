from django.shortcuts import render
from .models import Price
import plotly.graph_objects as go
from django.shortcuts import render
import json

# Create your views here.

def time_diagram(request):
    prices = Price.objects.order_by('created')
    # Prepare data for plotting
    price_values = [price.price for price in prices][int(len(prices) / 2):]
    created_values = [str(price.created) for price in prices][int(len(prices) / 2):]
    print(price_values)
    print(created_values)

    # Pass the data to the template
    context = {
        'price_values': price_values,
        'created_values': created_values,
    }
    return render(request, 'index.html', context=context)
