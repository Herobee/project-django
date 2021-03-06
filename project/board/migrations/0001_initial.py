# Generated by Django 2.2.7 on 2019-11-25 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_idx', models.AutoField(primary_key=True, serialize=False)),
                ('board_title', models.CharField(max_length=45)),
                ('board_content', models.TextField()),
                ('read_count', models.IntegerField(default=0)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('usr_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
