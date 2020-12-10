# Generated by Django 3.0.4 on 2020-12-10 23:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0027_auto_20201210_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 23, 16, 54, 457694, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 12, 10, 23, 16, 54, 458692, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 23, 16, 54, 455672, tzinfo=utc), null=True),
        ),
    ]
