from rest_framework import serializers
from .models import sparkToken

class sparkTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = sparkToken
        fields = '__all__'