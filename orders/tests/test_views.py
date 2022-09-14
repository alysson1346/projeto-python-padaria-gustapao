from itertools import product
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from accounts.models import Account
from products.models import Category, Product
from ..models import Order

import ipdb


class OrdersViewsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.client: APIClient
        cls.admin_user_data = {"username": "Superuser", "email": "superuser@mail.com", "password": "1234",
                               "first_name": "Client", "last_name": "client", "cellphone": "02199990900", "is_superuser": True}
        cls.admin_user = Account.objects.create_user(**cls.admin_user_data)

        cls.common_user_data = {"username": "Cleint 1", "email": "test@mail.com", "password": "1234",
                                "first_name": "Client", "last_name": "client", "cellphone": "02199999900"}
        cls.common_user = Account.objects.create_user(**cls.common_user_data)

        cls.admin_token = Token.objects.create(user=cls.admin_user)
        cls.common_token = Token.objects.create(user=cls.common_user)


        cls.category_1, _ = Category.objects.get_or_create(
            **{"name": "Pastel"})
        cls.category_2, _ = Category.objects.get_or_create(**{"name": "Bolo"})
        cls.category_3, _ = Category.objects.get_or_create(
            **{"name": "Salgado"})

        cls.product_1_data = {"name": "pastel peq", "price": 10}
        cls.product_1 = Product.objects.create(**cls.product_1_data)

        cls.product_2_data = {"name": "pastel grande",
                              "price": 20, "category": cls.category_2}
        cls.product_2 = Product.objects.create(**cls.product_2_data)

        cls.product_3_data = {"name": "pastel de vento",
                              "price": 5, "category": cls.category_3}
        cls.product_3 = Product.objects.create(**cls.product_3_data)

        cls.order_1_data = {
            "comment": "comentario 2....",
            "withdrawal_date": "2022-09-15",
            "products": [
                {"product": cls.product_1.id, "quantity": 3},
                {"product": cls.product_2.id, "quantity": 2},
                {"product": cls.product_3.id, "quantity": 5}
            ]
        }

        # cls.base_order_url = reverse('base-order-url')
        cls.base_create_url = reverse('base-order-create-url')
        # cls.base_detail_url = reverse('detail-order-url', kwargs={'pk': cls})
        # cls.base_update_status_url = reverse('update-status')


    # def test_list_all_orders(self):
    #     token = self.admin_token.__dict__["key"]
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    #     expected_status_code = status.HTTP_200_OK
    #     response = self.client.get(self.base_order_url)
    #     self.assertEquals(expected_status_code, response.status_code)

    def test_create_order(self):
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_create_url, data=self.order_1_data)
        self.assertEquals(expected_status_code, response.status_code)
        ...
