# Generated by Django 3.2.25 on 2024-07-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q1bapp', '0026_auto_20240713_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
