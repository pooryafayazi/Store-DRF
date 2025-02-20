from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class ProductStatusType(models.IntegerChoices):
    draft = 1, 'draft'
    published = 2, 'published'
    archived = 3, 'archived'

class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ProductModel(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    category = models.ManyToManyField('ProductCategoryModel')
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(default='/default/product-image.jpg', upload_to='product/img/%Y/%m/%d/')
    brief_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    # status = models.IntegerField(choices=[(1, 'draft'), (2, 'published'), (3, 'archived')], default=1)
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.draft.value)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_show_price(self):
        # return self.price - (self.price * self.discount_percent / 100)
        return '{:,}'.format(round((self.price - (self.price * self.discount_percent / 100)) / 1000) * 1000)
    
    def is_discounted(self):
        return self.discount_percent > 0
        # return self.discount_percent != 0
    
    def get_show_raw_price(self):
        return '{:,}'.format(self.price)
    
class Meta:
    ordering = ['-created_date']

class ProdoctImageModel(models.Model):
    product = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='product/extra-img/%Y/%m/%d/')
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product