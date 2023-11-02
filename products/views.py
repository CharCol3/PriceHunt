from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Store, Product, PriceEntry, UserPoints
from .serializers import StoreSerializer, ProductSerializer, PriceEntrySerializer, UserPointsSerializer

# Store Views
class StoreListCreateView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Price Entry Views
class PriceEntryListCreateView(generics.ListCreateAPIView):
    queryset = PriceEntry.objects.all()
    serializer_class = PriceEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

class PriceEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceEntry.objects.all()
    serializer_class = PriceEntrySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

# User Points Views
class UserPointsListView(generics.ListAPIView):
    queryset = UserPoints.objects.all()
    serializer_class = UserPointsSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class UserPointsDetailView(generics.RetrieveAPIView):
    queryset = UserPoints.objects.all()
    serializer_class = UserPointsSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
