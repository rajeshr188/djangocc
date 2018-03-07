# Generated by Django 2.0.2 on 2018-03-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girvi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='CreatedBy',
        ),
        migrations.RemoveField(
            model_name='license',
            name='OwnedBy',
        ),
        migrations.AlterField(
            model_name='customer',
            name='RelatedAs',
            field=models.CharField(choices=[('s/o', 's/o'), ('d/o', 'd/o'), ('w/o', 'w/o')], default='s/o', max_length=3),
        ),
    ]
