from rest_framework import serializers
from second.models import Phone_number, Subscribe, Company, Company_Phone_List 

# using model serializer 
class PhoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Phone_number
		fields = '__all__' 

class SubscribeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscribe
		fields = '__all__' 

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'

class Company_Phone_ListSerializer(serializers.ModelSerializer):
	phone = PhoneSerializer()

	class Meta:
		model = Company_Phone_List
		fields = ['name', 'phone']

	# create is ovewritten as it has complex relationships 
	def create(self, validated_data):
		phone = validated_data.pop('phone')
		phone_obj = Phone_number.objects.create(**phone)
		company_phone = Company_Phone_List.objects.create(phone=phone_obj, **validated_data)
		return company_phone