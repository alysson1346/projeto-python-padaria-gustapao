from django.test import TestCase
from ..models import Category
# Create your tests here.
class CategoriesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.category_data_1 = { "name": "Category 1"}
        cls.category_data_2 = { "name": "Category 2"}
        cls.category_data_3 = { "name": "Category 3"}
        cls.category_1 = Category.objects.create(**cls.category_data_1)
        cls.category_2 = Category.objects.create(**cls.category_data_2)
        cls.category_3 = Category.objects.create(**cls.category_data_3)

    def test_db_Categories_length(self):
        database_length = len(Category.objects.all())
        self.assertEqual(database_length, 3)


    def test_username_max_length(self):
        category = Category.objects.get(name="Category 1")
        max_length = category._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


    def test_Category_unique_name(self):
        test_1 = {"name": "Category 1"}
        Category.objects.get_or_create(**test_1)
        database_length = len(Category.objects.all())
        self.assertEqual(database_length, 3)


    def test_categories_field(self):
        self.assertEqual(self.category_1.name, self.category_data_1['name'], "name diferent")