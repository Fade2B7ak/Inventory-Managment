# Generated by Django 4.1.5 on 2023-02-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_inventory_data_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='Confirm your password here', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='Enter your password here', max_length=50),
        ),
    ]
