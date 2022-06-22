from django.urls import path
from . import views

urlpatterns = [
    path('api/service/', views.ServiceList.as_view())
    
]