from django.urls import path, include
from second.views import home, phoneViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('phone', phoneViewset, basename='vs')

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls))
]