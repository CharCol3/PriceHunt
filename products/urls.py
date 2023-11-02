from django.urls import path
from .views import (
    StoreListCreateView,
    StoreDetailView,
    ProductListCreateView,
    ProductDetailView,
    PriceEntryListCreateView,
    PriceEntryDetailView,
    UserPointsListView,
    UserPointsDetailView,
)

urlpatterns = [
    path('stores/', StoreListCreateView.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('price-entries/', PriceEntryListCreateView.as_view(), name='price-entry-list'),
    path('price-entries/<int:pk>/', PriceEntryDetailView.as_view(), name='price-entry-detail'),
    path('user-points/', UserPointsListView.as_view(), name='user-points-list'),
    path('user-points/<int:pk>/', UserPointsDetailView.as_view(), name='user-points-detail'),
]
