# Generated by Django 4.0.6 on 2022-09-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApisUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
