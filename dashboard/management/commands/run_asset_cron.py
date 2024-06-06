from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from dashboard.models import Asset
import yfinance as yf

class Command(BaseCommand):
    help = 'Executa a tarefa cron para um ativo específico'

    def add_arguments(self, parser):
        parser.add_argument('ticker', help='Ticker do ativo a ser monitorado')

    def handle(self, *args, **kwargs):
        asset_ticker = kwargs['ticker']
        asset = Asset.objects.get(ticker=asset_ticker)
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
