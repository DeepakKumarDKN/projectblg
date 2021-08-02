from django.urls import path
from blogapp import views_api

urlpatterns=[
  path('login/', views_api.LoginView),
  path('register/', views_api.RegisterView)
]