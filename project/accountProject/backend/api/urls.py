from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]