from django.test import TestCase
from ..models import Ingredient


# Create your tests here.
class IngredientsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.ingredient_data_1 = {"name": "ingredient 1"}
        cls.ingredient_data_2 = {"name": "ingredient 2"}
        cls.ingredient_data_3 = {"name": "ingredient 3"}
        cls.ingredient_1 = Ingredient.objects.create(**cls.ingredient_data_1)
        cls.ingredient_2 = Ingredient.objects.create(**cls.ingredient_data_2)
        cls.ingredient_3 = Ingredient.objects.create(**cls.ingredient_data_3)


    def test_db_Ingredients_length(self):
        database_length = len(Ingredient.objects.all())
        self.assertEqual(database_length, 3)


    def test_username_max_length(self):
        ingredient = Ingredient.objects.get(name="ingredient 1")
        max_length = ingredient._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


    def test_Ingredients_unique_name(self):
        test_1 = {"name": "ingredient 1"}
        Ingredient.objects.get_or_create(**test_1)
        database_length = len(Ingredient.objects.all())
        self.assertEqual(database_length, 3)


    def test_Ingredients_field(self):
        self.assertEqual(self.ingredient_1.name, self.ingredient_data_1['name'], "name diferent")


