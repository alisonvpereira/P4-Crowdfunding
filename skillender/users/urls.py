from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('create-profile/', views.CustomUserList.as_view()),
    path('users/', views.CustomUserList.as_view()),
    path('users/<str:username>', views.ProfileView.as_view())
    

]

urlpatterns = format_suffix_patterns(urlpatterns)