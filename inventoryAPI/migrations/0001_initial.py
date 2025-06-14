# Generated by Django 5.2.1 on 2025-05-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('barcode', models.IntegerField(unique=True)),
            ],
        ),
    ]
