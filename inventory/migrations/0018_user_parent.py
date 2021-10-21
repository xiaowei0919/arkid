# Generated by Django 3.2.6 on 2021-08-27 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_merge_20210823_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='父账号'),
        ),
    ]
