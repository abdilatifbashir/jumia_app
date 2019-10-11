from django.contrib import admin
from .models import Product, Category, Subcategory


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'subcategory')
#     list_filter = ("category,subcategory",)
#     prepopulated_fields = {'slug': ('name',)}
    
#     admin.site.register(Product, ProductAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

#     admin.site.register(Category, CategoryAdmin)
   




# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'comission', 'quantity', ]
#     prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Category, CategoryAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Subcategory)
