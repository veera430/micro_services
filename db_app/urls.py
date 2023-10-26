from django.urls import path, include
from .views import *
from rest_framework .routers import DefaultRouter

router = DefaultRouter()
#register
router.register(r'api', UserDetails_viewset)
urlpatterns = [
    path('', include(router.urls)),
]