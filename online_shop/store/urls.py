from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CategoryListAPIView,
                    SubCategoryViewSet, ProductListAPIView,
                    ProductDetailAPIView,ProductImageViewSet, ReViewViewSet,
                    CartViewSet, CartItemViewSet, CategoryDetailAPIView)

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'SubCategory', SubCategoryViewSet)
router.register(r'ProductImage', ProductImageViewSet)
router.register(r'ReView', ReViewViewSet)
router.register(r'Cart', CartViewSet)
router.register(r'CartItem', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
]