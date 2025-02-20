from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
from random import choice
import random
from django.core.files import File
from ...models import ProductModel, ProductCategoryModel, ProductStatusType
from accounts.models import User, UserType

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = 'Create fake ProductModel entries'

    IMAGE_LIST = [
        'images/image1.jpg',
        'images/image2.jpg',
        'images/image3.jpg',
        'images/image4.jpg',
        'images/image5.jpg',
        'images/image6.jpg',
        'images/image7.jpg',
    ]

    def handle(self, *args, **kwargs):
        faker = Faker()
        superusers = User.objects.filter(type=UserType.superuser.value)

        if superusers.exists():  # Check if there are any superusers
            user = choice(superusers)  # Randomly select one superuser
        else:
            self.stdout.write(self.style.ERROR('No superusers found. Exiting...'))
            return

        categories = ProductCategoryModel.objects.all()

        for _ in range(10):
            # title = faker.catch_phrase()
            title = faker.word()
            slug = slugify(title, allow_unicode=True)
            selected_category = random.sample(list(categories), random.randint(1, 4))
            selected_image = choice(self.IMAGE_LIST)
            image_obj = File(open(BASE_DIR / selected_image, 'rb'), name=Path(selected_image).name)
            brief_description = faker.paragraph(nb_sentences=3)
            # brief_description = faker.sentence(nb_words=10)
            description = faker.text()
            stock = faker.random_int(min=0, max=100)
            price = faker.random_int(min=10, max=10000) * 1000
            discount_percent = faker.random_int(min=0, max=50)

            product = ProductModel.objects.create(
                user=user,
                title=title,
                slug=slug,
                image=image_obj,
                brief_description = brief_description,
                description=description,
                stock=stock,
                status=ProductStatusType.published.value,
                # status=choice(ProductStatusType.choices)[0],
                price=price,
                discount_percent=discount_percent
            )
            
            product.category.set(selected_category)

        self.stdout.write(self.style.SUCCESS('Successfully created fake ProductModel entries.'))