# Generated by Django 2.0.2 on 2018-03-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girvi', '0013_auto_20180302_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanbill',
            name='ItemValue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='loanbill',
            name='ItemWeight',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=7),
        ),
        migrations.AlterField(
            model_name='loanbill',
            name='LoanAmount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10),
        ),
    ]
