# Generated by Django 3.0.5 on 2020-06-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='Description',
            field=models.CharField(blank=True, default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='cv',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
    ]