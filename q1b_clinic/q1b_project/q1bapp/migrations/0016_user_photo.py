# Generated by Django 3.2.25 on 2024-07-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q1bapp', '0015_patient_register_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]