# Generated by Django 3.0.2 on 2020-09-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='licenseNumber',
            field=models.CharField(default='null', max_length=150, verbose_name='License number'),
        ),
    ]
