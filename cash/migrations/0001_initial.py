# Generated by Django 2.2.4 on 2019-08-21 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='Physical Cash', max_length=256)),
                ('currency', models.CharField(blank=True, default='GHC', max_length=64)),
                ('balance', models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=20)),
                ('comment', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CashIncrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='Physical Cash', max_length=256)),
                ('currency', models.CharField(default='GHC', max_length=64)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tempa', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('cash', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cash.Cash')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CashDecrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(default='Physical Cash', max_length=256)),
                ('currency', models.CharField(default='GHC', max_length=64)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tempa', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=256)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('cash', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cash.Cash')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
