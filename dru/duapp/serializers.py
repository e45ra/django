from rest_framework import serializers
from .models import Drug,Store,Stores,Cage,PersonData

class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        
class CageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = '__all__'