from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    )

from .models import ProductModel, ProductStatusType, ProcuctCategoryModel, ProdoctImageModel
# Create your views here.


class ShopProductGridView(ListView):
    template_name = 'shop/product-grid.html'
    queryset = ProductModel.objects.filter(status=ProductStatusType.published.value)