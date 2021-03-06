""" flink_api URL Configuration """

# Django
from collections import namedtuple
from django.contrib import admin
from django.urls import path, include

# Views
from companies.views import CompanyViewSet

# Django REST framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
