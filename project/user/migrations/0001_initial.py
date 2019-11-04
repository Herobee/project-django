# Generated by Django 2.2.6 on 2019-11-04 09:36

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('usr_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('usr_pwd', models.CharField(max_length=45)),
                ('usr_name', models.CharField(max_length=45, unique=True)),
                ('usr_email', models.CharField(max_length=45)),
                ('usr_phone', models.CharField(max_length=45)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usr_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('usr_name', models.CharField(max_length=45, unique=True)),
                ('usr_email', models.CharField(max_length=45, unique=True)),
                ('usr_phone', models.CharField(max_length=45, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user.models.MyUserManager()),
            ],
        ),
    ]