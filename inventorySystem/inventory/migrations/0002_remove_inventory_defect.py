# Generated by Django 4.1.5 on 2023-01-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='defect',
        ),
    ]