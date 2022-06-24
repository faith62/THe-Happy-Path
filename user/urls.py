from django.urls import path
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('clientlist/', views.ClientProfileList.as_view()),
    path('clientprofile/<int:pk>/', views.ClientProfileDetail.as_view()),
    path('client/registration/',views.user_registration),
    path('client/login/',views.user_login),    
    path('api/counselor/', views.CounselorList.as_view()),
    path('api/counselor/<int:pk>/', views.showcounselor,name='counselor'),

]

urlpatterns = format_suffix_patterns(urlpatterns)