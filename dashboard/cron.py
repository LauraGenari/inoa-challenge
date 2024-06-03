# dashboard/cron.py

from django_cron import CronJobBase, Schedule
import yfinance as yf

from django.core.mail import send_mail
from django.conf import settings

from dashboard.models import Asset

class CheckPricesCronJob(CronJobBase):      
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'dashboard.check_prices_cron_job'  # Identificador único

    def do(self):
        assets = Asset.objects.all()
        for asset in assets:
            ticker = yf.Ticker(asset.ticker)
            current_price = ticker.history(period="1d")['Close'].iloc[-1]
            if current_price < asset.lower_tunnel:
                send_mail(
                    'Oportunidade de Compra',
                    f'O preço do ativo {asset.ticker} está abaixo do limite inferior do túnel: {current_price}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.NOTIFICATION_EMAIL]
                )
            elif current_price > asset.upper_tunnel:
                send_mail(
                    'Oportunidade de Venda',
                    f'O preço do ativo {asset.ticker} está acima do limite superior do túnel: {current_price}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.NOTIFICATION_EMAIL]
                )

