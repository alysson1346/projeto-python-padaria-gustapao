import json
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from products.models import Product
from products.models import Category
from products.models import Ingredient
from accounts.models import Account
import ipdb

class ProductViewsTests(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.client: APIClient

        cls.common_user = {
			"username": "common",
			"password": "1234",
			"email": "common@mail.com",
			"first_name": "co",
			"last_name": "client",
			"cellphone": "02199999999"
		}

        cls.staff_user = {
			"username": "employee",
			"password": "9999",
			"email": "emplyee@mail.com",
			"first_name": "em",
			"last_name": "ployee",
			"cellphone": "0110000000",
   			"is_staff": True,
		}

        cls.admin_user = {
            "username": "admin",
            "password": "3333",
            "email": "admin@mail.com",
            "first_name": "ad",
            "last_name": "min",
            "cellphone": "01177777777",
            "is_superuser": True,
        }

        cls.common_credentials = {
            "username": "common",
            "password": "1234",
        }

        cls.staff_credentials = {
            "username": "employee",
            "password": "9999",
        }

        cls.admin_credentials = {
            "username": "admin",
            "password": "3333",
        }

        cls.common_account= Account.objects.create_user(**cls.common_user)
        cls.common_token = Token.objects.create(user=cls.common_account)
        cls.staff_account= Account.objects.create_user(**cls.staff_user)
        cls.staff_token = Token.objects.create(user=cls.staff_account)
        cls.admin_account= Account.objects.create_user(**cls.admin_user)
        cls.admin_token = Token.objects.create(user=cls.admin_account)

        cls.product_obj1 = {
            "name": "Pão Doce",
            "price": 100,
            "description":"string bem longa e desnecessaria",
        }
        cls.category_obj = {
            "name": "Panificadora"
        }
        cls.category_1 = Category.objects.create(**cls.category_obj)

        cls.product_1 = Product.objects.create(**cls.product_obj1, category=cls.category_1)

        cls.ingredients_obj = {
            "name": "Farinha"
        }
        cls.ingredients_1= Ingredient.objects.create(**cls.ingredients_obj)
        cls.ingredients_1.products.add(cls.product_1)
        cls.ingredients_1.save()

        cls.base_product_url = reverse("list-create")
        cls.base_product_manage_details_url = reverse("retrieve-update-delete", kwargs={'pk': cls.product_1.id})


    def test_empty_fields_create_product(self):
        test_request = {}

        expected_status_code = status.HTTP_400_BAD_REQUEST

        response = self.client.post(self.base_product_url, data=test_request)

        self.assertEquals(expected_status_code, response.status_code)

    def test_common_user_cannot_create_product(self):
        # token = self.common_token.__dict__["key"]
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        test_request = {
            "name": "Bolo",
            "price": 10,
            "description":"string bem longa e desnecessaria",
            "ingredients": [{"name": "Ovo"}],
            "category": {"name": "Ovo"},
        }

        expected_status_code = status.HTTP_403_FORBIDDEN

        response = self.client.post(self.base_product_url, data=test_request, format='json')
        # ipdb.set_trace()

        self.assertEquals(expected_status_code, response.status_code)