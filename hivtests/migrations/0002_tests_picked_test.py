# Generated by Django 3.1.1 on 2020-09-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivtests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='picked_test',
            field=models.CharField(default=False, max_length=3),
        ),
    ]
