# Generated by Django 4.0.4 on 2022-05-06 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0002_catdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='ing_type',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='cat_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='instaapp.catdetails'),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='meal',
            field=models.CharField(default='allmeals', max_length=50),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='prep_time',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='rec_desc',
            field=models.CharField(default='null', max_length=300),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='rec_type',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AddField(
            model_name='recipe_detail',
            name='serve_people',
            field=models.SmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ing_name',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe_detail',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
