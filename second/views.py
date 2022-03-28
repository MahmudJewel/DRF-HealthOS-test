from django.shortcuts import render
from django.http import HttpResponse
from second.models import Phone_number, Subscribe
from second.serializers import PhoneSerializer, SubscribeSerializer
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