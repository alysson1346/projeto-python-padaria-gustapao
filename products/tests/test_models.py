from rest_framework.test import APITestCase, APIClient
from ..models import Product

class ProductModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client: APIClient

        cls.product_obj = {
            "name": "Pão Doce",
            "price": 100,
            "description":"string bem longa e desnecessaria",
            "is_available": False,
        }
        cls.product_1 = Product.objects.create(**cls.product_obj)

    #Faltando testes de relacionamentos

    #Atribute Tests
    def test_product_fields(self):
        self.assertEqual(self.product_1.name, self.product_obj["name"])
        self.assertEqual(self.product_1.price, self.product_obj["price"])
        self.assertEqual(self.product_1.description, self.product_obj["description"])
        self.assertEqual(self.product_1.is_available, self.product_obj["is_available"])

    def test_name_max_lenth(self):
        expected = 50
        result = self.product_1._meta.get_field("name").max_length
        msg = f"Verify max_length of {self.product_1.name}"

        self.assertEqual(result, expected, msg)

    def test_description_blank_default_value(self):
        expected = True
        result = self.product_1._meta.get_field("description").blank
        msg = f"Verify default value of blank in description"

        self.assertEqual(result, expected, msg)

    def test_description_null_default_value(self):
        expected = True
        result = self.product_1._meta.get_field("description").null
        msg = f"Verify default value of null in description"

        self.assertEqual(result, expected, msg)

    def test_price_max_digits(self):
        expected = 8
        result = self.product_1._meta.get_field("price").max_digits
        msg = f"Verify max_digits of price field"

        self.assertEqual(result, expected, msg)

    def test_price_decimal_places(self):
        expected = 2
        result = self.product_1._meta.get_field("price").decimal_places
        msg = f"Verify decimal_places of price field"

        self.assertEqual(result, expected, msg)

    def test_is_available_default_value(self):
        expected = True
        result = self.product_1._meta.get_field("is_available").default
        msg = f"Verify default value of is_available field"

        self.assertEqual(result, expected, msg)

    def test_is_available_value(self):
        expected = False
        result = self.product_1._meta.get_field("is_available").value=False
        msg = f"Verify value of is_available field"

        self.assertEqual(result, expected, msg)
