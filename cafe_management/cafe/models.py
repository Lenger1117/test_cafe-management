from django.db import models

class Order(models.Model):
    ORDER_STATUS = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.PositiveSmallIntegerField()
    items = models.JSONField(default=list)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='waiting')

    def save(self, *args, **kwargs):
        self.total_price = sum(item['price'] * item['quantity'] for item in self.items)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Заказ №{self.id} - Стол {self.table_number}"
