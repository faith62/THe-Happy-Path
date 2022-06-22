from django.urls import path,include
from . import views 
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('contact',ContactViewSet)


urlpatterns = [
    path('',include(router.urls)),
]