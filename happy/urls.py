from django.urls import path
from . import views

urlpatterns = [
    path('api/contact/', views.contactList.as_view()),
    path('api/contact/<int:pk>', views.contact_detail, name='contact'),
    
]