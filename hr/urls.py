from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_changelist'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='product_change'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]
