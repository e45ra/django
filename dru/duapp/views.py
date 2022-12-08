from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Cage, Store, Drug, PersonData
from rest_framework import viewsets
from .serializers import PersonDataSerializer, DrugSerializer, StoreSerializer, CageSerializer

class PersonDataView(viewsets.ModelViewSet):
    serializer_class = PersonDataSerializer
    queryset = PersonData.objects.all()

class DrugView(viewsets.ModelViewSet):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    
class StoreView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    
class CageView(viewsets.ModelViewSet):
    serializer_class = CageSerializer
    queryset = Cage.objects.all()