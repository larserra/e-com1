
from django.urls import path
from .import views


urlpatterns = [
   
    path('', views.store, name='store' ),
    path('<slug:c_slug>/', views.store, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.product_detail, name='product_detail'),
] 

