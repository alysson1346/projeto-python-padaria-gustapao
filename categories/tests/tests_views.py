import django
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from accounts.models import Account
from ..models import Categories

# Create your tests here.
class CategoriesViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client: APIClient

        # cls.admin_user = {
		# 	"username": "test3",
		# 	"password": "3333",
		# 	"email": "test3@mail.com",
		# 	"first_name": "test3",
		# 	"last_name": "Employee",
		# 	"cellphone": "01177777777",
   		# 	"is_superuser": True,
		# }

        cls.category_data_1 = {	"title": "Category 1"}
        cls.category_data_2 = {	"title": "Category 2"}
        cls.category_data_3 = {	"title": "Category 3"}

        cls.category_1 = Categories.objects.create(**cls.category_data_1)
        cls.category_2 = Categories.objects.create(**cls.category_data_2)
        cls.category_3 = Categories.objects.create(**cls.category_data_3)

        cls.base_category_url = reverse('list-categories')
        cls.base_get_category_pk_url = reverse('category_detail', kwargs={'pk': cls.category_1.id})

    #     cls.admin_account= Account.objects.create_user(**cls.admin_user)
    #     cls.admin_token = Token.objects.create(user=cls.admin_account)

    # def test_empty_create_category(self):
    #     test_request = {}
    #     expected_status_code = status.HTTP_400_BAD_REQUEST
    #     response = self.client.post(self.base_category_url, data=test_request)
    #     self.assertEquals(expected_status_code, response.status_code)
