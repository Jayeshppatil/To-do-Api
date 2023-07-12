from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/',views.loginPage,name="login"), 
    path('logout/',views.logoutUser,name="logout"),
	path('', views.list, name="list"),

]
