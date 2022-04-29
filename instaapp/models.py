# Create your models here.

from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, ImageField, IntegerField

# Create your models here.
'''
class catdetails(models.Model):
    catid=models.AutoField(primary_key=True)
    diet=models.CharField(max_length=50)
    main_ing=models.CharField(max_length=50)
    cuisine=models.CharField(max_length=50)
    rcptype=models.Model(CharField)

class Recipe_detail(models.Model):
    rcpid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    catid = models.ForeignKey(catdetails, default=0)
    preptime=models.IntegerField(default=5)
    cooktime=models.IntegerField(default=5)
    servings=models.IntegerField(default=2)
    short_desc=models.CharField(max_length=200)
    img = models.ImageField(upload_to='recipe_imgs')
    difficulty=models.IntegerChoices()

    

class Ingredients(models.Model):
    ing_id=models.AutoField(primary_key=True)
    ing_name = models.CharField(max_length=100)
    ing_type=models.CharField(max_length=50)
    cal_count=models.IntegerField(default=50)
    qty_type=models.IntegerField(default=1)

    def __str__(self):
        return self.ingr_name

class steps(models.Model):
    rcp_id = models.AutoField(primary_key=True)
    step_num = models.IntegerField()
    step_desc = models.CharField(max_length=200)
    step_time = models.IntegerField()
    ingr_qty = models.ForeignKey(Ingredients)

'''

'''
class shoppinglist(models.Model):
	user_id
	ingr_id
	quantity
	shop_date

8)Feedback
	-rating
	-comment
	-date
	-recipe_id
	-user_id '''

class Recipe_detail(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='recipe_imgs')

class Ingredients(models.Model):
    
    ing_name = models.CharField(max_length=100)
    def __str__(self):
        return self.ingr_name
