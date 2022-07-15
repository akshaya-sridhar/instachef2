# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class catdetails(models.Model):
    cat_name = models.CharField(max_length=50, default="categoryname")
    cat_img = models.ImageField(upload_to="static/cat_img")

    def __str__(self):
        return self.cat_name

# sample not working
class Recipe_detail(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="null")
    rec_type = models.CharField(max_length=10, default="null")
    prep_time = models.SmallIntegerField(default=5)
    serve_people = models.SmallIntegerField(default=2)
    meal = models.CharField(max_length=50, default="allmeals")
    rec_desc = models.CharField(max_length=300, default="null")
    img = models.ImageField(upload_to='recipe_imgs')
    cat_name = models.ForeignKey(catdetails, on_delete=models.DO_NOTHING)

class Ingredients(models.Model):
    ing_name = models.CharField(max_length=100)
    ing_option = [('Recipe Base', 'Recipe Base'),
                  ('Vegetables & Greens','Vegetables & Greens'),
                  ('Fruits & Berries','Fruits & Berries'),
                  ('Meat','Meat'),
                  ('Baking','Baking'),
                 ('Dairy & Eggs','Dairy & Eggs'),
                 ('Herbs & Spices','Herbs & Spices'),
                 ]
    ing_type = models.CharField(max_length=50,choices=ing_option,default='Vegetable & Green')

    def __str__(self):
        return self.ing_name

class getingredients(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.DO_NOTHING)
    ing_name = models.ForeignKey(Ingredients, null=True, on_delete=models.DO_NOTHING)

class Recipe_info(models.Model):
    name = models.CharField(max_length=100)
   
    rec_option =  [('veg','Veg'),
                ('non-veg', 'Non-Veg'),
                ('vegan','Vegan')]

    rec_type = models.CharField(max_length=10,choices=rec_option,null=True)
    prep_time = models.IntegerField()
    serve_people = models.IntegerField()
    img = models.ImageField(upload_to='static/img')
    cat_name = models.ForeignKey(catdetails,default = 1,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Recipe_step(models.Model):
    name = models.ForeignKey(Recipe_info,on_delete=models.DO_NOTHING)
    step_no = models.IntegerField()
    step_desc = models.CharField(max_length=200)
    ingr = models.ForeignKey(Ingredients,on_delete=models.DO_NOTHING)
    qty = models.IntegerField(null=True)

    def __str__(self):
        return self.step_desc



class requestrecipe(models.Model):

    VEG = 'VEG'
    NONVEG = 'NVEG'
    VEGAN = 'VEGAN'

    REC_TYPE = [
        (VEG, 'Vegetarian'),
        (NONVEG, 'Non Vegetarian'),
        (VEGAN, 'Vegan')
    ]
    Recipe_name = models.CharField(max_length=100)
    Recipe_type = models.CharField(
        max_length=5, choices=REC_TYPE)
    Category_name = models.ForeignKey(
        catdetails, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Recipe_name

class userfeedback(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.DO_NOTHING)
    Feedback= models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.Feedback

