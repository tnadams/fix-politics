# Generated by Django 3.0.8 on 2020-08-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0017_auto_20200808_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='key',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
