from django.urls import path
from . import views


urlpatterns =[
    path(r'',views.prod,name='prod'),
    path('add',views.new_product,name='new_product'),
    path('csv',views.download_csv,name='download_csv'),
    path('clear',views.clear_data,name='clear_data'),
]
