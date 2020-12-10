# Generated by Django 3.0.4 on 2020-12-10 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0017_auto_20201210_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 9, 11, 15, 601955, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 12, 10, 9, 11, 15, 602953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 9, 11, 15, 599960, tzinfo=utc), null=True),
        ),
    ]
