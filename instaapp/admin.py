from django.contrib import admin

from instaapp.models import Ingredients, Recipe_detail

# Register your models here.
admin.site.register(Recipe_detail)
admin.site.register(Ingredients)
