# Generated by Django 5.1.6 on 2025-02-24 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0003_alter_custfeedback_first_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustFeedback',
            new_name='Cust_Feedback',
        ),
    ]
