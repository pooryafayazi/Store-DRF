from django.urls import path, include
from . import views

app_name ='shop'

urlpatterns = [
    path('product/grid/', views.ShopProductGridView.as_view(), name='product-grid' ),

]