from .models import Tv
from rest_framework import serializers

class TvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tv
        fields = '__all__'