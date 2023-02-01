# Generated by Django 4.1.5 on 2023-01-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemClass', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('defect', models.TextField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock_date', models.DateField(auto_now_add=True)),
                ('ready_to_load', models.BooleanField(default=False)),
                ('data_update', models.DateField(auto_now=True)),
            ],
        ),
    ]
