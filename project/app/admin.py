from django.contrib import admin

# Register your models here.
from .models import Variant, Product,ProductImage,ProductVariant,ProductVariantPrice

admin.site.register(Variant)