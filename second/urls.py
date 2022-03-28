from django.urls import path, include
from second.views import home, phoneViewset, subscribeViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('phone', phoneViewset, basename='phone')
router.register('sub', subscribeViewset, basename='sub')

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls))
]