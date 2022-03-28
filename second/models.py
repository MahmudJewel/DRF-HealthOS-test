from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Phone_number(models.Model):
    phone_regex = RegexValidator(regex=r'^(?:\+88|88)?(01[3-9]\d{8})$', message="Phone number must be entered in the format: '+8801XXXXXX'. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, unique=True) # custom validation is used rather than phone field. as Phone field has large memory size. 
    def __str__(self):
        return self.phone_number
    
class Subscribe(models.Model):
    planList=[('Bronze', 'Globalnet Bronze'),
                ('Silver', 'Globalnet Silver'),
                ('Gold', 'Globalnet Gold'),]  
    
    plan = models.CharField(max_length=20, choices=planList, default='Bronze') # As the plans are fixed, so I used choices field
    phone = models.OneToOneField(Phone_number, on_delete=models.CASCADE)
    dateOfBuy = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.phone

class Company(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Company_Phone_List(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASECADE)
    phone = models.ForeignKey(Phone_number, on_delete=models.CASCADE)