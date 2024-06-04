# dashboard/forms.py
from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['ticker', 'lower_tunnel', 'upper_tunnel', 'check_period']
        labels = {
            'ticker': 'Código do Ativo',
            'lower_tunnel': 'Limite Inferior',
            'upper_tunnel': 'Limite Superior',
            'check_period': 'Período de Verificação (em minutos)',
        }
        widgets = {
            'ticker': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: PETR4.SA'}),
            'lower_tunnel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex: 36.75'}),
            'upper_tunnel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex: 40.15'}),
            'check_period': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2'}),
        }
