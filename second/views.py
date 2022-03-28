from django.shortcuts import render
from django.http import HttpResponse
from second.models import Phone_number, Subscribe, Company, Company_Phone_List
from second.serializers import PhoneSerializer, SubscribeSerializer, CompanySerializer, Company_Phone_ListSerializer
from rest_framework import viewsets

# Create your views here.

def home(request):
    return HttpResponse('Hello World!!!')

# viewsets for create, update and delete phone numbers
class phoneViewset(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
	"""
	serializer_class = PhoneSerializer
	queryset = Phone_number.objects.all()

# viewsets for subscriptions plans
class subscribeViewset(viewsets.ModelViewSet):
	serializer_class = SubscribeSerializer
	queryset = Subscribe.objects.all()

# It will add company name
class CompanyViewset(viewsets.ModelViewSet):
	serializer_class = CompanySerializer
	queryset = Company.objects.all()

# This will add multiple phone numbers for specific company
class Company_Phone_ListViewset(viewsets.ModelViewSet):
	serializer_class = Company_Phone_ListSerializer
	queryset = Company_Phone_List.objects.all()