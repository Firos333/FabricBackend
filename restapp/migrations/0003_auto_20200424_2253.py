# Generated by Django 3.0.5 on 2020-04-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200424_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarytable',
            name='Unique_id',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
    ]
