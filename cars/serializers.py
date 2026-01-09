from rest_framework import serializers
from .models import Car, Category


class CarSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Car
        fields = [
            'id',
            'category',
            'category_id',
            'brand',
            'model',
            'year',
            'price',
            'created_at'
        ]