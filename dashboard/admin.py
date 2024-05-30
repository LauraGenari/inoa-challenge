from django.contrib import admin
from .models import Asset, PriceRecord

admin.site.register(Asset)
admin.site.register(PriceRecord)
