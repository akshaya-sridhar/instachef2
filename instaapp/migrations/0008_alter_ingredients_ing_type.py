# Generated by Django 4.0.4 on 2022-05-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0007_alter_ingredients_ing_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ing_type',
            field=models.CharField(choices=[('Recipe Base', 'Recipe Base'), ('Vegetables & Greens', 'Vegetables & Greens'), ('Fruits & Berries', 'Fruits & Berries'), ('Meat', 'Meat'), ('Baking', 'Baking'), ('Dairy & Eggs', 'Dairy & Eggs'), ('Herbs & Spices', 'Herbs & Spices')], default='Vegetable & Green', max_length=50),
        ),
    ]