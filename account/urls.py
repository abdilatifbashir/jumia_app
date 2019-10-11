from django.urls import re_path, path
from . import views

app_name = 'account'

urlpatterns = [
    re_path(r'^$', views.user_login, name='login'),
    re_path(r'^dashboard/', views.dashboard, name='dashboard'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),

]
