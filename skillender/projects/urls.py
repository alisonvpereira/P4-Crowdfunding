from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('skills/', views.SkillList.as_view()),
    path('skills/<int:pk>', views.SkillDetail.as_view()),
    path('projects/<int:pk>', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    # path('pledges/<int:pk>', views.PledgeDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)