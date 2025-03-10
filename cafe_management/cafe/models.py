from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

class Order(models.Model):
    ORDER_STATUS = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.PositiveSmallIntegerField()
    items = models.ManyToManyField(Item, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='waiting')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_price = sum(item.price for item in self.items.all())
        super().save(update_fields=['total_price'])
    
    def __str__(self):
        return f"Заказ №{self.id} - Стол {self.table_number}"
