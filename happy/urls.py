from django.urls import path
from . import views

urlpatterns = [
    path('api/counselor/', views.CounselorList.as_view()),
    path('api/counselor/<int:pk>/', views.CounselorDetail.as_view()),
]
