from rest_framework import serializers
from .models import Variant, Product,ProductImage,ProductVariant,ProductVariantPrice

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant, Product,ProductImage,ProductVariant,ProductVariantPrice
        fields = '__all__'