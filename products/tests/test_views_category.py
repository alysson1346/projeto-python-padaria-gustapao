from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from accounts.models import Account
from ..models import Category
# Create your tests here.
class CategoriesViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client: APIClient
        cls.admin_user = {
            "username": "test3",
            "password": "3333",
            "email": "test3@mail.com",
            "first_name": "test3",
            "last_name": "Employee",
            "cellphone": "01177777777",
            "is_superuser": True,
        }
        cls.common_user = {
            "username": "test1",
            "password": "1234",
            "email": "test1@mail.com",
            "first_name": "test",
            "last_name": "client",
            "cellphone": "02199999999"
        }
        cls.category_data_1 = { "name": "Category 1"}
        cls.category_data_2 = { "name": "Category 2"}
        cls.category_data_3 = { "name": "Category 3"}
        cls.category_1 = Category.objects.create(**cls.category_data_1)
        cls.category_2 = Category.objects.create(**cls.category_data_2)
        cls.category_3 = Category.objects.create(**cls.category_data_3)
        cls.base_category_url = reverse('list-categories')
        cls.base_get_category_pk_url = reverse('category_detail', kwargs={'pk': cls.category_1.id})
        cls.admin_account= Account.objects.create_user(**cls.admin_user)
        cls.admin_token = Token.objects.create(user=cls.admin_account)
        cls.common_account= Account.objects.create_user(**cls.common_user)
        cls.common_token = Token.objects.create(user=cls.common_account)
    def test_list_all_categories(self):
        expected_status_code = status.HTTP_200_OK
        response = self.client.get(self.base_category_url)
        self.assertEquals(expected_status_code, response.status_code)


    def test_superuser_wrong_fields_category(self):
        token = self.admin_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {}
        expected_status_code = status.HTTP_400_BAD_REQUEST
        response = self.client.post(self.base_category_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_admin_can_create_category(self):
        token = self.admin_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category test admin"}
        expected_status_code = status.HTTP_201_CREATED
        response = self.client.post(self.base_category_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_common_user_cannot_create_category(self):
        token = self.common_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category test common create"}
        expected_status_code = status.HTTP_403_FORBIDDEN
        response = self.client.post(self.base_category_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_admin_can_update_category(self):
        token = self.admin_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category updated"}
        expected_status_code = status.HTTP_200_OK
        response = self.client.patch(self.base_get_category_pk_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_common_user_cannot_update_category(self):
        token = self.common_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category test common update"}
        expected_status_code = status.HTTP_403_FORBIDDEN
        response = self.client.patch(self.base_category_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_admin_can_delete_category(self):
        token = self.admin_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category updated"}
        expected_status_code = status.HTTP_204_NO_CONTENT
        response = self.client.delete(self.base_get_category_pk_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)


    def test__only_common_user_cannot_delete_category(self):
        token = self.common_token.__dict__["key"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        test_request = {"name": "Category test common delete"}
        expected_status_code = status.HTTP_403_FORBIDDEN
        response = self.client.delete(self.base_category_url, data=test_request)
        self.assertEquals(expected_status_code, response.status_code)