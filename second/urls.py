from django.urls import path, include
from second.views import home, phoneViewset, subscribeViewset,CompanyViewset, Company_Phone_ListViewset

# router 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('phone', phoneViewset, basename='phone')
router.register('sub', subscribeViewset, basename='sub')
router.register('company', CompanyViewset, basename='company')
router.register('company-phone', Company_Phone_ListViewset, basename='company')

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls))
]