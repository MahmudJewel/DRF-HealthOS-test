from django.urls import path, include
from second.views import home
urlpatterns = [
    path('', home, name='home'),
]