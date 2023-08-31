from django.test import TestCase, RequestFactory
from restaurant import models
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        models.Menu.objects.create(id="1", title="borgir", price=1, inventory=100)
        models.Menu.objects.create(id="2", title="pissa", price=2, inventory=300)

    def test_get_all(self):
        items_in_db = models.Menu.objects.all()
        serialized_items_in_db = MenuSerializer(items_in_db, many=True)

        request = self.factory.get("/restaurant/menu/")
        response = MenuItemView.as_view()(request)

        self.assertEqual(
            serialized_items_in_db.data,
            response.data,
        )
