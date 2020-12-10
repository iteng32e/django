# Generated by Django 3.0.4 on 2020-12-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201210_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='method',
            field=models.CharField(blank=True, choices=[('On', 'Online'), ('Off', 'Offline')], default='On', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1, null=True),
        ),
    ]
