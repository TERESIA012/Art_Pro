# Generated by Django 3.2.8 on 2021-10-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.CharField(default='admin', max_length=70),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]