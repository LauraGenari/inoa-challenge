# Generated by Django 5.0.6 on 2024-06-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='check_period',
            field=models.IntegerField(),
        ),
    ]
