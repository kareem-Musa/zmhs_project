# Generated by Django 3.1.1 on 2020-12-21 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20201212_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='locality',
            options={'verbose_name_plural': 'Localities'},
        ),
        migrations.AlterModelOptions(
            name='unity',
            options={'verbose_name_plural': 'Unities'},
        ),
    ]