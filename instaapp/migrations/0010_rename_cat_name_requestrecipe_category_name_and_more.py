# Generated by Django 4.0.4 on 2022-05-13 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0009_alter_recipe_detail_cat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestrecipe',
            old_name='cat_name',
            new_name='Category_name',
        ),
        migrations.RenameField(
            model_name='requestrecipe',
            old_name='rrec_name',
            new_name='Recipe_name',
        ),
        migrations.RenameField(
            model_name='requestrecipe',
            old_name='rrec_type',
            new_name='Recipe_type',
        ),
    ]