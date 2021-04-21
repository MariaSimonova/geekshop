from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command

from authapp.models import User
from basket.models import Basket
from mainapp.models import Product, ProductCategory


class TestCreateBasket(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')

        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

        self.client.login(username='tarantino', password='geekbrains')

        self.category = ProductCategory.objects.create(name="Новый бренд")

        self.product = Product.objects.create(name="Пальто",
                                              category=self.category,
                                              price=2000.00,
                                              quantity=2)

        self.basket = Basket.objects.create(user=self.user,
                                            product=self.product,
                                            quantity=1)

    def test_basket_get(self):
        basket_product = Basket.objects.get(product="Пальто")
        product = Product.objects.get(name="Пальто")

        self.assertEqual(product, basket_product)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')
