from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CatAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CatAdmin)

class ProAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','updated','created']
    list_editable=['stock','price','available']
    prepopulated_fields={'slug':('name',)}
    list_per_page=22
admin.site.register(Product,ProAdmin)
