# Generated by Django 3.2.8 on 2021-11-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_sync', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasyncconfig',
            name='name',
            field=models.CharField(default='', max_length=128, unique=True, verbose_name='配置名称'),
        ),
    ]
