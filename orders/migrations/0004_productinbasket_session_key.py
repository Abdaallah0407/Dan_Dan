# Generated by Django 3.1.6 on 2021-03-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_productinbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
