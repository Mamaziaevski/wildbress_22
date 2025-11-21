from .models import(UserProfile, Category, SubCategory,
                    Product, ProductImage, ReView,
                    Cart, CartItem)
from .serializers import(UserProfileSerializers, CategoryListSerializers, CategoryDetailSerializers,SubCategorySerializers,
                    ProductListSerializers,ProductDetailSerializers, ProductImageSerializers, ReViewSerializers,
                    CartSerializers, CartItemSerializers)
from rest_framework import viewsets, generics

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers

class ReViewViewSet(viewsets.ModelViewSet):
    queryset = ReView.objects.all()
    serializer_class = ReViewSerializers

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers

