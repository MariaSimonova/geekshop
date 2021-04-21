from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command


class TestAuthappSmoke(TestCase):

    def setUp(self):
        # call_command('flush', '--noinput')
        # call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_authapp_urls(self):
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/profile/')
        self.assertEqual(response.status_code, 200)



    # def tearDown(self):
    #     call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')
