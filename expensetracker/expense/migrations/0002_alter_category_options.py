# Generated by Django 4.2.3 on 2023-07-21 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
