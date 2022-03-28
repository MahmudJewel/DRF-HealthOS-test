from django.contrib import admin
from second.models import Phone_number, Subscribe

lst = [Phone_number, Subscribe]
admin.site.register(lst)
