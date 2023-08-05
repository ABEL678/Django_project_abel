from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'product_name': 'Рубанок', 'price': '2520,50', 'category': 'Инструменты', 'description': 'большой'},
            {'product_name': 'Киянка', 'price': '520,30', 'category': 'Инструменты', 'description': 'деревянная'},
            {'product_name': 'Гвоздь', 'price': '1,50', 'category': 'Крепеж', 'description': '4,0*100 оцинкованный'},
            {'product_name': 'Винт', 'price': '12,30', 'category': 'Крепеж', 'description': 'М12х65'},
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_for_create)
