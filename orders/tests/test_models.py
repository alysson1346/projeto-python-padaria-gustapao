import ipdb
from accounts.models import Account
from django.test import TestCase
from products.models import Category, Ingredient, Product

from ..models import Order


class OrdersModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.superuser_data = {"username": "Superuser", "email": "superuser@mail.com", "password": "1234", "first_name": "Client", "last_name": "client","cellphone": "02199990900"}
        cls.superuser = Account.objects.create_superuser(**cls.superuser_data)
        cls.client_data_1 = {"username": "Cleint 1", "email": "test@mail.com", "password": "1234", "first_name": "Client", "last_name": "client","cellphone": "02199999900"}
        cls.client_1 = Account.objects.create_user(**cls.client_data_1)
        cls.ingredient_data_1 = {"name": "ovo"}
        cls.ingredient_data_2 = {"name": "farinha"}
        cls.ingredient_data_3 = {"name": "pinga"}
        cls.ingredient_1 = Ingredient.objects.create(**cls.ingredient_data_1)
        cls.ingredient_2 = Ingredient.objects.create(**cls.ingredient_data_2)
        cls.ingredient_3 = Ingredient.objects.create(**cls.ingredient_data_3)
        cls.category_1,_ = Category.objects.get_or_create(**{"name": "Pastel"})
        cls.category_2,_ = Category.objects.get_or_create(**{"name": "Bolo"})
        cls.category_3,_ = Category.objects.get_or_create(**{"name": "Salgado"})
        cls.product_1_data = {"name": "pastel peq", "price": 10}
        cls.product_2_data = {"name": "pastel grande", "price": 20, "category": cls.category_2}
        cls.product_3_data = {"name": "pastel de vento", "price": 5, "category": cls.category_3}
        cls.product_1 = Product.objects.create(**cls.product_1_data)
        cls.product_2 = Product.objects.create(**cls.product_2_data)
        cls.product_3 = Product.objects.create(**cls.product_3_data)
        cls.order_data_1 = {"comment":"Comment test 1", "withdrawal_date": "2050-09-28", "account": cls.client_1}
        cls.order_data_2 = {"comment":"Test 2 comment", "withdrawal_date": "2050-09-29", "account": cls.client_1}
        cls.order_data_3 = {"comment":"Test 2 comment", "withdrawal_date": "2050-09-22", "account": cls.client_1}
        cls.order_1 = Order.objects.create(**cls.order_data_1)
        cls.order_2 = Order.objects.create(**cls.order_data_2)
        cls.order_3 = Order.objects.create(**cls.order_data_3)
        cls.order_1.products.add(cls.product_1, through_defaults={"quantity": 3})
        cls.order_2.products.add(cls.product_2, through_defaults={"quantity": 5})
        cls.order_3.products.add(cls.product_3, through_defaults={"quantity": 1})
        
    def test_db_orders_length(self):
        database_length = len(Order.objects.all())
        self.assertEqual(database_length, 3)
        
    def test_order_status_max_length(self):
        order = Order.objects.all()[1]
        max_length = order._meta.get_field("order_status").max_length
        self.assertEqual(max_length, 50)
        
    def test_total_max_length(self):
        order = Order.objects.all()[1]
        max_length = order._meta.get_field("total").max_digits
        self.assertEqual(max_length, 10)
        
    def test_total_decimal_places(self):
        order = Order.objects.all()[1]
        max_length = order._meta.get_field("total").decimal_places
        self.assertEqual(max_length, 2)
        
    def test_order_status_choice_recused(self):
        order = Order.objects.all()[1]
        order.order_status = "Pedido Recusado"
        order.save()
        order_recused = order = Order.objects.get(id=order.id)
        self.assertEqual(order_recused.order_status, "Pedido Recusado")
        
    def test_order_status_choice_accepted(self):
        order = Order.objects.all()[1]
        order.order_status = "Pedido Confirmado"
        order.save()
        order_recused = order = Order.objects.get(id=order.id)
        self.assertEqual(order_recused.order_status, "Pedido Confirmado")
        
    def test_order_status_choice_accepted(self):
        order = Order.objects.all()[1]
        order.order_status = "Status inválido"
        order.save()
        order_recused = order = Order.objects.get(id=order.id)
        self.assertEqual(order_recused.order_status, order.order_status)
        
    def test_orders_field(self):
        self.assertEqual(self.order_1.comment, self.order_data_1['comment'], "comment diferent")
        self.assertEqual(self.order_1.withdrawal_date, self.order_data_1['withdrawal_date'], "withdrawal_date diferent")
        
    def test_order_relation_account_and_order(self):
        self .assertEqual(self.order_1.account, self.client_1, "account diferent of expected")
        
    def test_retations_order_products(self):
        clien_test_data = {"username": "Client test", "email": "test_client@mail.com", "password": "1234", "first_name": "Client test", "last_name": "client","cellphone": "02166699900"}
        client_test = Account.objects.create_user(**clien_test_data)
        order_test_data = {"comment":"Order test 1",    "withdrawal_date": "2050-12-30", "account": client_test}
        order_test = Order.objects.create(**order_test_data)
        order_test.products.add(self.product_1, through_defaults={'quantity': 2})
        order_test.products.add(self.product_2, through_defaults={'quantity': 1})
        order_test.products.add(self.product_3, through_defaults={'quantity': 5})
        order_client_test = Order.objects.all()
        products_order = order_client_test[3].products.all()
        self.assertEqual(products_order[0].name, self.product_1.name)
        self.assertEqual(products_order[1].name, self.product_2.name)
        self.assertEqual(products_order[2].name, self.product_3.name)
