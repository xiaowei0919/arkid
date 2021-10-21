# Generated by Django 3.1.6 on 2021-03-05 08:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_app_type'),
        ('schema', '0002_auto_20210220_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('endpoint', models.CharField(max_length=1024, null=True)),
                ('token', models.CharField(blank=True, max_length=256, null=True)),
                ('mode', models.IntegerField(choices=[(0, 'Automatic')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Enabled'), (1, 'Disabled')], default=1)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.app')),
                ('schemas', models.ManyToManyField(blank=True, to='schema.Schema')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
