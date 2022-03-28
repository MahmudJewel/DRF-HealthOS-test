from django.shortcuts import render
from django.http import HttpResponse
from second.models import Phone_number, Subscribe, Company, Company_Phone_List
from second.serializers import PhoneSerializer, SubscribeSerializer, CompanySerializer, Company_Phone_ListSerializer
from rest_framework import viewsets

# Create your views here.

def home(request):
    return HttpResponse('Hello World!!!')

class phoneViewset(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
	"""
	serializer_class = PhoneSerializer
	queryset = Phone_number.objects.all()

class subscribeViewset(viewsets.ModelViewSet):
	serializer_class = SubscribeSerializer
	queryset = Subscribe.objects.all()

class CompanyViewset(viewsets.ModelViewSet):
	serializer_class = CompanySerializer
	queryset = Company.objects.all()

class Company_Phone_ListViewset(viewsets.ModelViewSet):
	serializer_class = Company_Phone_ListSerializer
	queryset = Company_Phone_List.objects.all()