from rest_framework import serializers
from .models import Mango, Order

class MangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
