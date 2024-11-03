from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('students', ListView, basename='student')
urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/',obtain_auth_token),
    path('auth/', include('rest_framework.urls')),
]
