from django.contrib import admin

from .models import ProductModel, ProcuctCategoryModel, ProdoctImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "stock", "status", "created_date"]
    searching_fields = ["id", "title", "status"]


@admin.register(ProcuctCategoryModel)
class ProcuctCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_date"]
    searching_fields = ["id", "title"]


@admin.register(ProdoctImageModel)
class ProdoctImageModelAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "created_date"]
    searching_fields = ["id", "product"]


"""
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(ProcuctCategoryModel, ProcuctCategoryModelAdmin)
admin.site.register(ProdoctImageModel, ProdoctImageModelAdmin)
"""