from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social_network import views


urlpatterns = [
    path('', views.api_root),
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)