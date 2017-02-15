from django.contrib import admin

from .models import Product, Category

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'slug', 'category', 'created')
    # list_filter = ('created', 'updated')
    prepopulated_fields = {'slug': ('name_en',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name_en',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
