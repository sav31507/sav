from django.contrib import admin

# Register your models here.
from . models import movie
class movieadmin(admin.ModelAdmin):
    list_display = ('name','year','image','des')
admin . site . register (movie,movieadmin)


