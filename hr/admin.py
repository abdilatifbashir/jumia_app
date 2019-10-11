from django.contrib import admin
from .models import Product, Category, Sub_category


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'Sub_category')
#     list_filter = ("category,Sub_category",)
#     prepopulated_fields = {'slug': ('name',)}
    
#     admin.site.register(Product, ProductAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

#     admin.site.register(Category, CategoryAdmin)
   




# class Sub_categoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'comission', 'quantity', ]
#     prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Category, CategoryAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sub_category)
