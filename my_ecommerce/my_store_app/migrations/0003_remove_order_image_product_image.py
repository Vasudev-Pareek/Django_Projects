# Generated by Django 5.1.3 on 2024-11-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_store_app', '0002_order_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
