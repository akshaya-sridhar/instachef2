from django.contrib import admin

from instaapp.models import Ingredients, Recipe_detail, Recipe_info, catdetails

# Register your models here.
# admin.site.register(Recipe_detail)
admin.site.register(Ingredients)
admin.site.register(Recipe_info)
admin.site.register(catdetails)
