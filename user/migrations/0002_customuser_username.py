# Generated by Django 4.0.6 on 2022-10-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
    ]
