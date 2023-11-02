from rest_framework import serializers
from .models import Store, Product, PriceEntry, UserPoints
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'barcode', 'created_at', 'updated_at')


class PriceEntrySerializer(serializers.ModelSerializer):
    reported_by = UserSerializer(read_only=True)

    class Meta:
        model = PriceEntry
        fields = ('id', 'product', 'store', 'price', 'date_reported', 'reported_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        # Get the user from the context
        user = self.context['request'].user

        # Check if the user is authenticated
        if user and user.is_authenticated:
            validated_data['reported_by'] = user
            price_entry = super().create(validated_data)

            # Award points for price report
            points_awarded = 10  # This could also be a setting or a calculated value
            UserPoints.objects.get_or_create(user=user)[0].add_points(points_awarded)

            return price_entry
        else:
            raise serializers.ValidationError("Users must be authenticated to create a price entry.")


class UserPointsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserPoints
        fields = ('id', 'user', 'total_points', 'created_at', 'updated_at')
