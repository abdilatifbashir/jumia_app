from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Jumia Vender Reconciler'
admin.site.site_title = 'Jumia'

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sub_category)
