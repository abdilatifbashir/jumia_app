from django.urls import re_path, path
from . import views

app_name = 'account'

urlpatterns = [
    re_path(r'^$', views.user_login, name='login'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            views.activate_account, name='activate'),
    re_path(r'^dashboard/', views.dashboard, name='dashboard'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),

]
