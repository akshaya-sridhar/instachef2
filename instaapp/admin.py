from django.contrib import admin

from instaapp.models import Ingredients, Recipe_detail, Recipe_info, catdetails, requestrecipe, Recipe_step, getingredients, userfeedback

# Register your models here.
# admin.site.register(Recipe_detail)
admin.site.register(Ingredients)
admin.site.register(Recipe_info)
admin.site.register(catdetails)
admin.site.register(requestrecipe)
admin.site.register(Recipe_step)
admin.site.register(getingredients)
admin.site.register(userfeedback)