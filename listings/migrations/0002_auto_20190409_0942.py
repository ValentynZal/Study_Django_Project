# Generated by Django 2.2 on 2019-04-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(default='New york', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=0),
        ),
    ]
