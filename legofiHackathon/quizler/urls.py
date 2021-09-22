from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
	path("oauth/", include("social_django.urls")),
	path('register/',views.register,name='register'),


]