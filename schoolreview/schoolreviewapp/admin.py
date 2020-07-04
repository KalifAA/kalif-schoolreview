from django.contrib import admin
from .models import School, SchoolImage, Comment
# Register your models here.

admin.site.register(School)
admin.site.register(SchoolImage)
admin.site.register(Comment)