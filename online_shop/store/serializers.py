from .models import *
from rest_framework import serializers

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileReViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']

class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_category_name']


class CategoryDetailSerializers(serializers.ModelSerializer):
    category_sub = SubCategorySerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'sub_category_name']




class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y_%H:%M:%S')
    product_images = ProductImageSerializers(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = [
            'id', 'product_name','price', 'product_images',
            'product_type', 'avg_rating', 'created_date', 'get_count_people',]

    def get_avg_rating(self, obj):
            return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class ReViewSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    user = UserProfileReViewSerializers()

    class Meta:
        model = ReView
        fields = ['user', 'text', 'stars', 'created_date']

class ProductDetailSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    product_images = ProductImageSerializers(read_only=True, many=True)
    subcategory = SubCategorySerializers()
    product_reviews = ReViewSerializers(read_only=True, many=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'product_name','subcategory','price','article_number','product_type','product_images',
            'description','video','created_date', 'product_reviews', 'get_count_people','avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'