# Generated by Django 3.0.4 on 2020-12-10 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0024_auto_20201210_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 11, 17, 5, 247139, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 12, 10, 11, 17, 5, 248133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 11, 17, 5, 245154, tzinfo=utc), null=True),
        ),
    ]
