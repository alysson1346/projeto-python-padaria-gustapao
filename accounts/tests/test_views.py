from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from accounts.models import Account


# Create your tests here.
class AccountViewTest(APITestCase):

	@classmethod
	def setUpTestData(cls):
		cls.client: APIClient

		cls.common_user = {
			"username": "test1",
			"password": "1234",
			"email": "test1@mail.com",
			"first_name": "test",
			"last_name": "client",
			"cellphone": "02199999999"
		}

		cls.staff_user = {
			"username": "test2",
			"password": "9999",
			"email": "test2@mail.com",
			"first_name": "test2",
			"last_name": "Employee",
			"cellphone": "0110000000",
   			"is_staff": True,
		}

		cls.admin_user = {
			"username": "test3",
			"password": "3333",
			"email": "test3@mail.com",
			"first_name": "test3",
			"last_name": "Employee",
			"cellphone": "01177777777",
   			"is_superuser": True,
		}

		cls.common_credentials = {
			"username": "test1",
			"password": "1234",
        }

		cls.staff_credentials = {
			"username": "test2",
			"password": "9999",
        }

		cls.admin_credentials = {
			"username": "test3",
			"password": "3333",
        }

		cls.common_account= Account.objects.create_user(**cls.common_user)
		cls.common_token = Token.objects.create(user=cls.common_account)
		cls.staff_account= Account.objects.create_user(**cls.staff_user)
		cls.staff_token = Token.objects.create(user=cls.staff_account)
		cls.admin_account= Account.objects.create_user(**cls.admin_user)
		cls.admin_token = Token.objects.create(user=cls.admin_account)

		cls.base_login_url = reverse("login")
		cls.base_account_url = reverse("account-view-create")
		cls.base_create_employee_url = reverse("create-employee")
		cls.base_account_retrive_delete_update_url = reverse("account-detail", kwargs={'pk': cls.common_account.id})
		cls.base_upgrade_admin_or_staff_url = reverse("admin-update", kwargs={'pk': cls.common_account.id})
		cls.base_patch_admin_soft_delete_url = reverse("soft-delete", kwargs={'pk': cls.common_account.id})


	def test_empty_create_account(self):
			test_request = {}
			expected_status_code = status.HTTP_400_BAD_REQUEST
			response = self.client.post(self.base_account_url, data=test_request)
			self.assertEquals(expected_status_code, response.status_code)


	def test_wrong_fields_account(self):
		test_request = {
            "user": "seller2",
            "password": "1234",
            "first": "sel2",
            "last": "ler2",
            "is_administrator": False
        }
		response = self.client.post(self.base_account_url, data=test_request)
		expected_status_code = status.HTTP_400_BAD_REQUEST
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_create_common_account(self):
		test_request = {
        	"username": "seller2",
			"password": "1234",
			"email": "test0@mail.com",
			"first_name": "test",
			"last_name": "client",
			"cellphone": "02199999999"
        }

		response = self.client.post(self.base_account_url, data=test_request)
		expected_status_code = status.HTTP_201_CREATED
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_create_staff_account(self):
		test_request = {
        	"username": "seller2",
			"password": "1234",
			"email": "test0@mail.com",
			"first_name": "test",
			"last_name": "client",
			"cellphone": "02199999999",
			"is_staff": True
        }

		response = self.client.post(self.base_account_url, data=test_request)
		expected_status_code = status.HTTP_201_CREATED
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_common_token_account(self):
			response = self.client.post(self.base_login_url, data=self.common_credentials)
			expected_token = self.common_token.__dict__["key"]
			result_token = response.data["token"]
			self.assertEqual(expected_token, result_token)


	def test_common_wrong_token_account(self):
			response = self.client.post(self.base_login_url, data=self.common_credentials)
			expected_token = "55abcf9e868a7cc8c34d8ae8683b63d22fd3c66b"
			result_token = response.data["token"]
			self.assertNotEqual(expected_token, result_token)


	def test_only_common_user_cannot_create_employee_account(self):
		token = self.common_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {
           "username": "test",
           "password": "1234",
           "first_name": "te",
           "last_name": "st",
           "is_staff": True,
           "email": "test222@mail.com",
			"cellphone": "0110800000",
        }
		response = self.client.post(self.base_create_employee_url, data=test_request)

		expected_status_code = status.HTTP_403_FORBIDDEN
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_only_admin_can_create_employee_account(self):
		token = self.admin_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {
           "username": "test",
           "password": "1234",
           "first_name": "te",
           "last_name": "st",
           "is_staff": True,
           "email": "test222@mail.com",
			"cellphone": "0110800000",
        }
		response = self.client.post(self.base_create_employee_url, data=test_request)
		expected_status_code = status.HTTP_201_CREATED
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_only_admin_retrieve_detail_account(self):
		token = self.admin_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		response = self.client.get(self.base_account_retrive_delete_update_url)
		expected_status_code = status.HTTP_200_OK
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)

	def test_only_common_retrieve_detail_account(self):
		token = self.common_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		response = self.client.get(self.base_account_retrive_delete_update_url)
		expected_status_code = status.HTTP_200_OK
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_common_user_cannot_update_account(self):
		token = self.common_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {"is_seller": True}
		response = self.client.patch(self.base_upgrade_admin_or_staff_url, data=test_request)
		expected_status_code = status.HTTP_403_FORBIDDEN
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_admin_user_can_update_to_adimin_account(self):
		token = self.admin_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {"is_seller": True}
		response = self.client.patch(self.base_upgrade_admin_or_staff_url, data=test_request)
		expected_status_code = status.HTTP_200_OK
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_admin_user_can_update_soft_delete_account(self):
		token = self.admin_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {"is_active": False}
		response = self.client.patch(self.base_upgrade_admin_or_staff_url, data=test_request)
		expected_status_code = status.HTTP_200_OK
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)


	def test_common_user_cannot_update_soft_delete_account(self):
		token = self.common_token.__dict__["key"]
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
		test_request = {"is_active": False}
		response = self.client.patch(self.base_upgrade_admin_or_staff_url, data=test_request)
		expected_status_code = status.HTTP_403_FORBIDDEN
		result_status_code = response.status_code
		self.assertEqual(expected_status_code, result_status_code)