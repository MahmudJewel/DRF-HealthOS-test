from rest_framework import serializers
from second.models import Phone_number, Subscribe

# using model serializer 
class PhoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Phone_number
		fields = '__all__' 

class SubscribeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscribe
		fields = '__all__' 