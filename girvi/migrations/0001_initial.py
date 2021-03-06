# Generated by Django 2.0.2 on 2018-02-28 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedOn', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=30)),
                ('RelatedAs', models.CharField(choices=[('s/o', 's/o'), ('d/o', 'd/o'), ('w/o', 'w/o')], max_length=3)),
                ('RelatedTo', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('Area', models.CharField(blank=True, max_length=20)),
                ('ContactNo', models.CharField(blank=True, max_length=10)),
                ('EmailId', models.EmailField(blank=True, max_length=254)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['CreatedOn'],
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedOn', models.DateTimeField(auto_now=True)),
                ('Type', models.CharField(choices=[('PBL', 'Pawn Brokers License'), ('GST', 'Goods & Service Tax')], default='PBL', max_length=3)),
                ('Name', models.CharField(help_text='write Licence name here', max_length=20, unique=True)),
                ('Address', models.TextField(help_text='write licence address here')),
                ('OwnedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['CreatedOn'],
            },
        ),
        migrations.CreateModel(
            name='LoanBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LoanDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('LoanId', models.CharField(help_text='loanid here', max_length=10)),
                ('ItemType', models.CharField(choices=[('G', 'gold item'), ('S', 'silver item'), ('B', 'bronze item'), ('O', 'other')], default='G', max_length=1)),
                ('ItemDesc', models.TextField()),
                ('ItemWeight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ItemValue', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('LoanAmount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('LoanInt', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'ordering': ['LoanDate'],
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('loanbill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='girvi.LoanBill')),
                ('ReleaseId', models.CharField(max_length=10, unique=True)),
                ('ReleaseDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('InterestPaid', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'ordering': ['ReleaseDate'],
            },
        ),
        migrations.AddField(
            model_name='loanbill',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girvi.Customer'),
        ),
        migrations.AddField(
            model_name='loanbill',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girvi.License'),
        ),
        migrations.AlterUniqueTogether(
            name='loanbill',
            unique_together={('license', 'LoanId')},
        ),
    ]
