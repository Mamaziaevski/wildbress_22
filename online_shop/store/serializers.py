from .models import *
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name','username','password',
                'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


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


class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image', 'category_sub']


class SubCategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','sub_category_name']



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


class SubCategoryDetailSerializers(serializers.ModelSerializer):
    products = ProductListSerializers(read_only=True, many=True)
    class Meta:
        model = SubCategory
        fields = ['sub_category_name', 'products']



class ReViewSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    user = UserProfileReViewSerializers()

    class Meta:
        model = ReView
        fields = ['user', 'text', 'stars', 'created_date']

class ProductDetailSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    product_images = ProductImageSerializers(read_only=True, many=True)
    subcategory = SubCategoryDetailSerializers()
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



class CartItemSerializers(serializers.ModelSerializer):
    product = ProductListSerializers(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                    write_only=True,source='product')
    total_price = serializers.SerializerMethodField()


    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()