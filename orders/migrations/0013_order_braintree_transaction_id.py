# Generated by Django 3.1.1 on 2021-01-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_order_braintree_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='braintree_transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]