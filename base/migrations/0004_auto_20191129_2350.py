# Generated by Django 2.2.7 on 2019-11-30 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20191129_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dresses',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
