from rest_framework import serializers
from cafe.models import Order, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']