# Generated by Django 3.0.4 on 2020-12-10 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201210_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, default='EXIST', max_length=9, null=True),
        ),
    ]