# Generated by Django 5.1.3 on 2024-12-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artic_App', '0009_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_name', models.CharField(max_length=100)),
                ('billing_email', models.EmailField(max_length=254)),
                ('billing_address', models.CharField(max_length=200)),
                ('billing_phone', models.CharField(max_length=15)),
                ('billing_message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Billing Address',
            },
        ),
    ]
