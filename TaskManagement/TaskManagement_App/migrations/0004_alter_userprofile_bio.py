# Generated by Django 5.1.3 on 2024-12-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement_App', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, default='To Do User', max_length=100, null=True),
        ),
    ]
