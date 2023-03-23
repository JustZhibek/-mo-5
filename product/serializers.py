from rest_framework import serializers
from product.models import Product, Category, Review

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializers(serializers.ReviewSerializer):
    class Meta:
        model = Review
        fields = '__all__'