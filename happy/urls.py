from django.urls import path
from . import views

urlpatterns = [
    path('api/service/', views.ServiceList.as_view()),
    path('api/service/<int:pk>', views.showservice, name='service'),
    
]