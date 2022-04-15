# Generated by Django 4.0.3 on 2022-04-15 08:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('url', models.CharField(blank=True, max_length=1024, verbose_name='url')),
                ('logo', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='logo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('type', models.CharField(max_length=128, verbose_name='type')),
                ('data', models.JSONField(blank=True, default=dict, verbose_name='data')),
                ('secret', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='secret')),
            ],
            options={
                'verbose_name': 'APP',
                'verbose_name_plural': 'APP',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('icon', models.URLField(blank=True, verbose_name='icon')),
            ],
            options={
                'verbose_name': 'tenant',
                'verbose_name_plural': 'tenant',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('username', models.CharField(max_length=128)),
                ('avatar', models.URLField(blank=True, verbose_name='Avatar')),
                ('is_platform_user', models.BooleanField(default=False, verbose_name='is platform user')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tenant')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'unique_together': {('username', 'tenant')},
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='core.usergroup')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tenant')),
                ('users', models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='core.user', verbose_name='User List')),
            ],
            options={
                'verbose_name': 'User Group',
                'verbose_name_plural': 'User Group',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TenantConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('token_duration_minutes', models.IntegerField(default=1440, verbose_name='Token Duration Minutes')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tenant', verbose_name='Tenant')),
            ],
            options={
                'verbose_name': 'Tenant Config',
                'verbose_name_plural': 'Tenant Config',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='users',
            field=models.ManyToManyField(related_name='tenant_user_set', related_query_name='user', to='core.user'),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('category', models.CharField(choices=[('entry', 'entry'), ('api', 'API'), ('data', 'data'), ('group', 'group'), ('ui', 'UI'), ('other', 'other')], default='other', max_length=100, verbose_name='category')),
                ('is_system', models.BooleanField(default=True, verbose_name='System Permission')),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.app', verbose_name='APP')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='core.permission', verbose_name='Parent')),
                ('permissions', models.ManyToManyField(blank=True, related_name='permission_set', related_query_name='permission', to='core.permission', verbose_name='Permission List')),
                ('tenant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.tenant', verbose_name='Tenant')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permission',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
                ('token', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Token')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='core.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Token',
            },
        ),
        migrations.CreateModel(
            name='Approve',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.CharField(choices=[('wait', 'Wait'), ('pass', 'Pass'), ('deny', 'Deny')], default='wait', max_length=100, verbose_name='Status')),
                ('data', models.JSONField(default=dict, verbose_name='Data')),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.app', verbose_name='APP')),
                ('tenant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.tenant', verbose_name='Tenant')),
            ],
            options={
                'verbose_name': 'Approve',
                'verbose_name_plural': 'Approve',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AppGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128)),
                ('apps', models.ManyToManyField(blank=True, related_name='app_set', related_query_name='app', to='core.app', verbose_name='APP List')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='core.appgroup')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tenant')),
            ],
            options={
                'verbose_name': 'APP Group',
                'verbose_name_plural': 'APP Group',
            },
            managers=[
                ('expand_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tenant'),
        ),
    ]
