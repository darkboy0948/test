# Generated by Django 3.1.1 on 2022-04-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRental', '0003_auto_20220416_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='FromDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ToDate',
            field=models.DateField(null=True),
        ),
    ]