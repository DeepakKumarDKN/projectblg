from django.urls import path 
from blogapp import views

urlpatterns = [
  path('',views.home, name="home"),
  path('add_blog/', views.add_blog, name="add_blog"),
  path('blog_detail/<slug>/', views.blog_detail, name="blog_detail"),
  path('see_blog/', views.see_blog, name="see_blog"),
  path('blog_delete/<id>/', views.blog_delete, name="blog_delete"),
  path('blog_update/<slug>/', views.blog_update, name="blog_update"),
  path('login/',views.login_view, name='login_view'),
  path('register/', views.register_view, name='register_view'),
  path('logout_view/',views.logout_view, name="logout_view")
 
]