# Generated by Django 2.2 on 2021-07-30 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='P_slug',
            new_name='slug',
        ),
    ]
