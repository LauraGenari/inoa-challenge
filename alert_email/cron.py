# alert_email/cron.py
from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from dashboard.models import Asset, PriceRecord
import requests
from datetime import datetime

class SendEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # define o intervalo em minutos

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'alert_email.send_emails_cron_job'  # um código único

    def do(self):
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
