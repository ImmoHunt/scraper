from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_title', 'item_content', 'item_published', 'item_series', 'item_slug')
