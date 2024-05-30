# alert_email/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from dashboard.models import Asset, PriceRecord
import requests
from datetime import datetime

@shared_task
def fetch_asset_prices():
    assets = Asset.objects.all()
    for asset in assets:
        response = requests.get(f'API_URL_FOR_PRICES/{asset.ticker}')
        data = response.json()
        current_price = data['price']

        PriceRecord.objects.create(asset=asset, price=current_price, timestamp=datetime.now())

        if current_price <= asset.lower_tunnel:
            send_mail(
                'Oportunidade de Compra',
                f'O preço do ativo {asset.ticker} está abaixo do limite inferior. Preço atual: {current_price}',
                'from@example.com',
                ['to@example.com']
            )
        elif current_price >= asset.upper_tunnel:
            send_mail(
                'Oportunidade de Venda',
                f'O preço do ativo {asset.ticker} está acima do limite superior. Preço atual: {current_price}',
                'from@example.com',
                ['to@example.com']
            )
