from rest_framework import serializers
from .models import MergedData

class MergedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MergedData
        fields = ['id', 'json_data', 'created_at']
