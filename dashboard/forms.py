# dashboard/forms.py
from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['ticker', 'lower_tunnel', 'upper_tunnel', 'check_period']
