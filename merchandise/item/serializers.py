from rest_framework import serializers
from item.models import Item,ItemDetails,ItemCategory


class ItemCategorySerializer(serializers.ModelSerializer):
    """Serializer for ItemCategory."""
    
    class Meta:
        model = ItemCategory
        fields = ('id', 'name', 'parent')


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for Item."""

    class Meta:
        model = Item
        fields = ('id', 'sku', 'price', 'size')


class ItemDetailsSerializer(serializers.ModelSerializer):
    """Serializer for ItemDetails which includes Item as 'sizes'."""
    
    sizes = ItemSerializer(many=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = ItemDetails
        fields = ('id', 'name', 'is_active', 'description', 'sizes', 'category')

    def get_category(self, obj):
        return obj.category.name