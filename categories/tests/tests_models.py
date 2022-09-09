from django.test import TestCase
from ..models import Categories

# Create your tests here.
class CategoriesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.category_data_1 = {	"title": "Category 1"}
        cls.category_data_2 = {	"title": "Category 2"}
        cls.category_data_3 = {	"title": "Category 3"}

        cls.category_1 = Categories.objects.create(**cls.category_data_1)
        cls.category_2 = Categories.objects.create(**cls.category_data_2)
        cls.category_3 = Categories.objects.create(**cls.category_data_3)

    def test_db_Categories_length(self):
        database_length = len(Categories.objects.all())
        self.assertEqual(database_length, 3)

    def test_username_max_length(self):
        category = Categories.objects.get(title="Category 1")
        max_length = category._meta.get_field("title").max_length
        self.assertEqual(max_length, 50)

    def test_Categories_unique_name(self):
        test_1 = {"title": "Category 1"}
        Categories.objects.get_or_create(**test_1)
        database_length = len(Categories.objects.all())
        self.assertEqual(database_length, 3)

    def test_categories_field(self):
        self.assertEqual(self.category_1.title, self.category_data_1['title'], "Title diferent")

