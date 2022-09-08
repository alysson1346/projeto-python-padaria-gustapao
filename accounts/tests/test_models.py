from xml.dom import ValidationErr
from django.test import TestCase
from ..models import Account
from django.db import IntegrityError

import ipdb


class AccountsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.common_user = {
            "username": "test1",
            "password": "1234",
            "email": "test1@mail.com",
            "first_name": "test",
            "last_name": "client",
            "cellphone": "02199999999",
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

        cls.common_account = Account.objects.create_user(**cls.common_user)
        cls.staff_account = Account.objects.create_user(**cls.staff_user)
        cls.admin_account = Account.objects.create_user(**cls.admin_user)


    def test_db_Accounts_length(self):
        database_length = Account.objects.all().length()
        self.assertEqual(database_length, 3)


    def test_username_max_length(self):
        user = Account.objects.get(username="test1")
        max_length = user._meta.get_field("username").max_length
        self.assertEqual(max_length, 50)


    def test_first_name_max_length(self):
        user = Account.objects.get(username="test1")
        max_length = user._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 50)


    def test_last_name_max_length(self):
        user = Account.objects.get(username="test1")
        max_length = user._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 50)


    def test_password_max_length(self):
        user = Account.objects.get(username="test1")
        max_length = user._meta.get_field("password").max_length
        self.assertEqual(max_length, 200)


    def test_cellphone_max_length(self):
        user = Account.objects.get(username="test1")
        max_length = user._meta.get_field("cellphone").max_length
        self.assertEqual(max_length, 12)

    def test_user_field(self) -> None:
        self.assertEqual(self.common_account.username,
                         self.common_user['username'], "Name diferent")
        self.assertEqual(self.common_account.email,
                         self.common_user['email'], "email diferent")
        self.assertEqual(self.common_account.first_name,
                         self.common_user['first_name'], "first_name diferent")
        self.assertEqual(self.common_account.last_name,
                         self.common_user['last_name'], "last_name diferent")
        self.assertEqual(self.common_account.cellphone,
                         self.common_user['cellphone'], "last_name diferent")
