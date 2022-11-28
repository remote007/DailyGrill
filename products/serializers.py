from rest_framework import serializers
from .models import ProductsTable

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsTable
        fields = '__all__'
