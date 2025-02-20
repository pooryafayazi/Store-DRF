from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
from ...models import ProductCategoryModel

class Command(BaseCommand):
    help = 'Create fake ProductCategoryModel entries'

    def handle(self, *args, **kwargs):
        faker = Faker()
        
        for _ in range(10):
            title = faker.word()
            slug = slugify(title, allow_unicode=True)
            
            # ProductCategoryModel.objects.get_or_create(title=title)
            
            # or Make sure the slug is unique if necessary
            while ProductCategoryModel.objects.filter(slug=slug).exists():
                slug = slugify(title, allow_unicode=True)
                
            ProductCategoryModel.objects.create(title=title, slug=slug)

        self.stdout.write(self.style.SUCCESS('Successfully created fake ProductCategoryModel entries.'))