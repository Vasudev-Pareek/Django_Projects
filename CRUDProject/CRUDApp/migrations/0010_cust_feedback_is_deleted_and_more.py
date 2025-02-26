# Generated by Django 5.1.6 on 2025-02-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0009_alter_cust_feedback_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cust_feedback',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cust_feedback',
            name='user_image',
            field=models.ImageField(blank=True, default='user_images/Avatar.png', null=True, upload_to='user_images/'),
        ),
    ]
