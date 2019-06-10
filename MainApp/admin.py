from django.contrib import admin
from .models import *


class FileUploadAdmin(admin.ModelAdmin):
    fields = ['name', 'file', 'add_time']


class ImageUploadAdmin(admin.ModelAdmin):
   fields = ['name', 'image', 'add_time']


admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(ImageUpload, ImageUploadAdmin)