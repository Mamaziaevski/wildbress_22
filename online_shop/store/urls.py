from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from .views import (UserProfileViewSet, CategoryListAPIView,
                    SubCategoryListSerializers, SubCategoryDetailSerializers, ProductListAPIView,
                    ProductDetailAPIView, ReViewViewSet,
                    CartViewSet, CartItemViewSet, CategoryDetailAPIView, SubCategoryListAPIView,
                    SubCategoryDetailAPIView,RegisterView, LoginView, LogoutView)
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'ReView', ReViewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('subcategory/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', CartViewSet.as_view(), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='cart_item_detail'),
]