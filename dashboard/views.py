from django.shortcuts import render, redirect
from .models import Asset, PriceRecord
from .forms import AssetForm

def index(request):
    assets = Asset.objects.all()
    return render(request, 'dashboard/index.html', {'assets': assets})

def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AssetForm()
    return render(request, 'dashboard/asset_form.html', {'form': form})

def edit_asset(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'dashboard/asset_form.html', {'form': form})

def price_history(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    price_records = PriceRecord.objects.filter(asset=asset).order_by('-timestamp')
    return render(request, 'dashboard/asset_list.html', {'asset': asset, 'price_records': price_records})
