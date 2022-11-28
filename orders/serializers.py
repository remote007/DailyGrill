from rest_framework import serializers
from .models import OrdersTable

class ComponentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdersTable
        fields = '__all__'
