# Generated by Django 2.0.2 on 2018-03-01 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girvi', '0010_auto_20180301_2354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
    ]
