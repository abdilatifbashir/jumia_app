from django.urls import path, re_path
from . import views



urlpatterns =[
    re_path(r'^$',views.prod,name='prod'),
    path('add',views.new_product,name='new_product'),
    path(r'csv/',views.export,name= 'export'),
    path(r'exel/',views.export_exel,name= 'export_exel'),
    path('clear',views.clear_data,name='clear_data'),
    path('clear/p',views.export_product_csv,name='export_product_csv'),
    re_path(r'^report/(?P<id>\d+)/', views.compare_csv_files, name='csv_report'),
]
