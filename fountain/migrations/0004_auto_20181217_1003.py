# Generated by Django 2.0.7 on 2018-12-17 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fountain', '0003_auto_20181217_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
