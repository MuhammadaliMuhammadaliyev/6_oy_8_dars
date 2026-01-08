from .models import Phones
from rest_framework import serializers

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'