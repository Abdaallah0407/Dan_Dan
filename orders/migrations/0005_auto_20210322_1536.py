# Generated by Django 3.1.6 on 2021-03-22 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_productinbasket_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_actived',
            new_name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
    ]
