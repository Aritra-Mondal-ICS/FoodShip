# Generated by Django 4.1.2 on 2022-11-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_userprofile_city_alter_userprofile_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='pin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]