from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Image)

# class ImageAdmian(admin.ModelAdmin):
# 	list_display=['id','photo','date']