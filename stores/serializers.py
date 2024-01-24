from rest_framework import serializers
from django.contrib.auth.models import User
from stores.models import Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id', 'created_at', 'name', 'rating', 'store_type', 'opening_hour',
            'closing_hour', 'city', 'latitude', 'longitude', 'location', 'address', 'phone',
        ]

class NearbyStoreSerializer(StoreSerializer):

    distance = serializers.SerializerMethodField()

    def get_distance(self, instance):
        return instance.distance.mi if instance else 'N/A'
    
    class Meta:
        model = Store
        fields = [
            'id', 'name', 'rating', 'opening_hour', 'closing_hour', 'store_type', 
            'address', 'latitude', 'longitude', 'distance',
        ]