from django.db import models

class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    lower_tunnel = models.DecimalField(max_digits=10, decimal_places=2)
    upper_tunnel = models.DecimalField(max_digits=10, decimal_places=2)
    check_period = models.IntegerField()

    def __str__(self):
        return self.ticker

class PriceRecord(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.ticker} - {self.price} em {self.timestamp}"
