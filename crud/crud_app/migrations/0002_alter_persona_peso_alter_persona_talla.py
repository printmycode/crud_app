# Generated by Django 4.2.3 on 2023-07-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='peso',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='persona',
            name='talla',
            field=models.CharField(max_length=10),
        ),
    ]