from item.models import Item, ItemDetails, ItemCategory
from item.serializers import ItemDetailsSerializer, ItemCategorySerializer, ItemSerializer

from rest_framework import viewsets

class ItemDetailsViewSet(viewsets.ModelViewSet):
    """Viewset for ItemDetails."""

    queryset = ItemDetails.objects.all()
    serializer_class = ItemDetailsSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Viewset for Item."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemCategoryViewSet(viewsets.ModelViewSet):
    """Viewset for ItemCategory."""
    
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
