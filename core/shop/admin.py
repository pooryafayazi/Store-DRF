from django.contrib import admin

from .models import ProductModel, ProductCategoryModel, ProdoctImageModel


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_date"]
    searching_fields = ["id", "title"]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "stock", "status", "price", "discount_percent" , "created_date"]
    searching_fields = ["id", "title", "status"]


@admin.register(ProdoctImageModel)
class ProdoctImageModelAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "created_date"]
    searching_fields = ["id", "product"]


"""
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(ProductCategoryModel, ProductCategoryModelAdmin)
admin.site.register(ProdoctImageModel, ProdoctImageModelAdmin)
"""