from django.urls import path
from . import views

urlpatterns = [
    path('api/contact/', views.contactList.as_view()),
    
]