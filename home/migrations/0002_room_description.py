# Generated by Django 2.0.2 on 2018-02-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(default='no description available...', max_length=300),
        ),
    ]
