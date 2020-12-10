# Generated by Django 3.0.4 on 2020-12-10 08:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20201210_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='championship',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.Member'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 8, 14, 4, 540730, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 12, 10, 8, 14, 4, 541727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 8, 14, 4, 538734, tzinfo=utc), null=True),
        ),
    ]
