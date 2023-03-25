from rest_framework import serializers
from product.models import Product, Category, Review

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ' id title description price category'.split()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = " id name product_list product_count".split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars product_title'.split()

class RatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()
