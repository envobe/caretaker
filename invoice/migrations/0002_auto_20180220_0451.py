# Generated by Django 2.0 on 2018-02-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoice',
            name='supplier_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='purchasereturninvoice',
            name='supplier_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='customer_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='salesreturninvoice',
            name='customer_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]