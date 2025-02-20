from django.db import models

# Create your models here.


class ProductStatus(models.IntegerChoices):
    draft = 1, 'draft'
    published = 2, 'published'
    archived = 3, 'archived'

class ProcuctCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ProductModel(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    category = models.ManyToManyField('ProcuctCategoryModel')
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(default='/default/product-image.jpg', upload_to='product/img/')
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    # status = models.IntegerField(choices=[(1, 'draft'), (2, 'published'), (3, 'archived')], default=1)
    status = models.IntegerField(choices=ProductStatus.choices, default=ProductStatus.draft.value)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    discount_percent = models.PositiveIntegerField(default=0)    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class ProdoctImageModel(models.Model):
    product = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='product/extra-img/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product