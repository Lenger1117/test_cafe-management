from django.test import TestCase
from .models import Order, Item

class OrderTestCase(TestCase):
    def setUp(self):
        # Тестовые данные
        self.item1 = Item.objects.create(name="Пицца", price=500)
        self.item2 = Item.objects.create(name="Сок", price=100)
        self.order = Order.objects.create(
            table_number=1,
            status="waiting"
        )
        self.order.items.add(self.item1, self.item2)

    def test_order_total_price(self):
        """Проверка корректности расчета total_price"""
        self.order.save()
        self.assertEqual(self.order.total_price, 600.0)

    def test_order_status_update(self):
        """Проверка изменения статуса"""
        new_status = "ready"
        self.order.status = new_status
        self.order.save()
        updated_order = Order.objects.get(id=self.order.id)
        self.assertEqual(updated_order.status, new_status)

    def test_order_deletion(self):
        """Проверка удаления заказа"""
        order_id = self.order.id
        self.order.delete()
        self.assertFalse(Order.objects.filter(id=order_id).exists())

    def test_order_creation(self):
        """Проверка создания заказа"""
        order_count = Order.objects.count()
        new_order = Order.objects.create(
            table_number=2,
            status="paid"
        )
        new_order.items.add(self.item2)
        self.assertEqual(Order.objects.count(), order_count + 1)
        self.assertEqual(new_order.status, "paid")

    def test_filter_by_status(self):
        """Проверка фильтрации заказов по статусу"""
        Order.objects.create(
            table_number=3,
            status="paid"
        )
        orders = Order.objects.filter(status="paid")
        self.assertEqual(orders.count(), 1)