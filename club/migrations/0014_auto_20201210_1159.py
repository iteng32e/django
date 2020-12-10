# Generated by Django 3.0.4 on 2020-12-10 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_auto_20201210_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 8, 29, 54, 448541, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 12, 10, 8, 29, 54, 448541, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 8, 29, 54, 448541, tzinfo=utc), null=True),
        ),
    ]