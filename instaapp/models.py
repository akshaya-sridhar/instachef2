# Create your models here.

from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class catdetails(models.Model):
    cat_name=models.CharField(max_length=50)
    cat_img=models.ImageField(upload_to="cat_img")

    def __str__(self):
        return self.cat_name


class Recipe_detail(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="null")
    rec_type=models.CharField(max_length=10, default="null")
    prep_time=models.SmallIntegerField(default=5)
    serve_people=models.SmallIntegerField(default=2)
    meal=models.CharField(max_length=50, default="allmeals")
    rec_desc=models.CharField(max_length=300, default="null")
    img = models.ImageField(upload_to='recipe_imgs')
    cat_name = models.ForeignKey(catdetails, default=1,on_delete=models.DO_NOTHING)

class Recipe_info(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="null")
    rec_type=models.CharField(max_length=10, default="null")
    prep_time=models.SmallIntegerField(default=5)
    serve_people=models.SmallIntegerField(default=2)
    meal=models.CharField(max_length=50, default="allmeals")
    rec_desc=models.CharField(max_length=300, default="null")
    img = models.ImageField(upload_to='recipe_imgs')
    cat_name = models.ForeignKey(catdetails, default=1,on_delete=models.DO_NOTHING)

class Ingredients(models.Model):
    
    ing_name = models.CharField(max_length=100, default="null")
    ing_type= models.CharField(max_length=50, default="null")
    def __str__(self):
        return self.ingr_name


    '''

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

