# Generated by Django 4.1.2 on 2022-10-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='names',
            field=models.CharField(max_length=250),
        ),
    ]
