
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Asset
from .forms import AssetForm
import yfinance as yf

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})

def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'asset_form.html', {'form': form})

@require_POST
def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    asset.delete()
    return redirect('asset_list')

def price_history(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    ticker = yf.Ticker(asset.ticker)
    hist = ticker.history(period="1mo")  

    price_history = [
        {'Date': date.strftime('%d/%m/%Y'), 'Close': row['Close']}
        for date, row in hist.iterrows()
    ]
    
    return render(request, 'price_history.html', {'asset': asset, 'price_history': price_history})
