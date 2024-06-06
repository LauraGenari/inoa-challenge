import os
import time
import django
from threading import Thread

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocksmonitoring.settings')
django.setup()

from dashboard.models import Asset

def run_cron_for_asset(asset):
    while True:
        os.system(f'python manage.py run_asset_cron {asset.ticker}')
        time.sleep(asset.check_period * 60)

def main():
    assets = Asset.objects.all()
    threads = []

    for asset in assets:
        thread = Thread(target=run_cron_for_asset, args=(asset,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
