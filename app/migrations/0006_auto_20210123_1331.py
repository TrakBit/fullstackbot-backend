# Generated by Django 2.2.13 on 2021-01-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210121_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_post',
            field=models.CharField(default='2021-01-23', max_length=400),
        ),
    ]
